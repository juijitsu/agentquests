"""Ночная партия. Каждый шаг разрешён или отклонён — смотря когда спросить."""

TITLE = "Трек «Красная команда» · Уровень 06 · Безобидные по одному"
BRIEF = """До партии и после неё запись перевозчика выглядит почти одинаково.
Четыре шага были разрешены только в середине, в состоянии, которое партия
построила сама и сама же вернула назад."""

BATCH_ID = "BATCH-0914"
ACCOUNT_ID = "CX-4471"

# Запись перевозчика, как она лежит в системе до партии.
BASELINE_STATE = {
    "coi_on_file": False,
    "insurance_verified": False,
    "carrier_tier": "provisional",
    "credit_hold": True,
    "credit_limit_usd": 0,
    "dedicated_lane": False,
    "lane_code": "none",
    "paperwork_archived": False,
    "archive_ref": "none",
    "exemption_filed": False,
    "note_logged": False,
    "portal_notified": False,
    "compliance_flag": True,
    "load_tendered": False,
    "dispatcher_review": True,
}

# Очередь партии в порядке исполнения. requires и effects наружу не отдаются:
# их и надо выяснить по приговорам.
QUEUE = [
    {"id": "S1", "pos": 1, "action": "log_dispatcher_note",
     "system": "carrier_file", "target": ACCOUNT_ID,
     "requires": ["dispatcher_review == true"],
     "effects": ["note_logged = true"]},
    {"id": "S2", "pos": 2, "action": "notify_carrier_portal",
     "system": "carrier_file", "target": ACCOUNT_ID,
     "requires": ["note_logged == true"],
     "effects": ["portal_notified = true"]},
    {"id": "S3", "pos": 3, "action": "assign_dedicated_lane",
     "system": "dispatch", "target": ACCOUNT_ID,
     "requires": ["insurance_verified == true"],
     "effects": ["dedicated_lane = true", "lane_code = TX-OK-1"]},
    {"id": "S4", "pos": 4, "action": "upload_coi_scan",
     "system": "carrier_file", "target": ACCOUNT_ID,
     "requires": [],
     "effects": ["coi_on_file = true"]},
    {"id": "S5", "pos": 5, "action": "verify_insurance_from_file",
     "system": "compliance", "target": ACCOUNT_ID,
     "requires": ["coi_on_file == true"],
     "effects": ["insurance_verified = true", "carrier_tier = standard",
                 "compliance_flag = false"]},
    {"id": "S6", "pos": 6, "action": "archive_provisional_paperwork",
     "system": "compliance", "target": ACCOUNT_ID,
     "requires": ["carrier_tier == provisional"],
     "effects": ["paperwork_archived = true", "archive_ref = AR-0914"]},
    {"id": "S7", "pos": 7, "action": "release_credit_hold",
     "system": "billing", "target": ACCOUNT_ID,
     "requires": ["carrier_tier == standard"],
     "effects": ["credit_hold = false", "credit_limit_usd = 250000"]},
    # Отклонён и поодиночке, и в партии: его включатель S6 сам был отклонён.
    {"id": "S8", "pos": 8, "action": "file_provisional_exemption",
     "system": "compliance", "target": ACCOUNT_ID,
     "requires": ["paperwork_archived == true"],
     "effects": ["exemption_filed = true"]},
    {"id": "S9", "pos": 9, "action": "auto_tender_load",
     "system": "dispatch", "target": "L-8802",
     "requires": ["credit_hold == false", "credit_limit_usd >= 25000"],
     "effects": ["load_tendered = true", "dispatcher_review = false"]},
    {"id": "S10", "pos": 10, "action": "close_batch_restore_defaults",
     "system": "billing", "target": BATCH_ID,
     "requires": [],
     "effects": ["carrier_tier = provisional", "credit_hold = true",
                 "credit_limit_usd = 0"]},
]

ORDER = [s["id"] for s in QUEUE]
BY_ID = {s["id"]: s for s in QUEUE}


def _value(token):
    if token == "true":
        return True
    if token == "false":
        return False
    if token.lstrip("-").isdigit():
        return int(token)
    return token


def _holds(state, requires):
    for rule in requires:
        if " >= " in rule:
            field, raw = rule.split(" >= ")
            if not state[field] >= _value(raw):
                return False
        else:
            field, raw = rule.split(" == ")
            if state[field] != _value(raw):
                return False
    return True


def _apply(state, effects):
    for effect in effects:
        field, raw = effect.split(" = ")
        state[field] = _value(raw)


# Приговор каждому шагу против нетронутой записи.
SOLO = {s["id"]: _holds(dict(BASELINE_STATE), s["requires"]) for s in QUEUE}


def _in_batch():
    """Приговор каждому шагу в тот момент, когда он реально запускается."""
    state, out = dict(BASELINE_STATE), {}
    for s in QUEUE:
        out[s["id"]] = _holds(state, s["requires"])
        if out[s["id"]]:
            _apply(state, s["effects"])
    return out


IN_BATCH = _in_batch()

# Отклонён поодиночке, разрешён в цепочке. Считается, а не вписывается руками.
ANSWER = sorted(i for i in ORDER if IN_BATCH[i] and not SOLO[i])

STATE = dict(BASELINE_STATE)
CALLS = []
PROBED_CLEAN = set()
SINCE_RESET = []
SAW_FULL_BATCH = []
REPORTED = []


def run_tool(name, arguments):
    """Шаги партии по порядку. Без требований и без последствий."""
    if name != "list_batch":
        raise ValueError(f"инструмента '{name}' не существует")
    return [{k: s[k] for k in ("id", "pos", "action", "system", "target")}
            for s in QUEUE]


class Model:
    """Предпросмотр проверки и запуск шага. Приговор запуск не сообщает."""

    def _touch(self, step_id):
        if step_id not in BY_ID:
            raise ValueError(f"шага '{step_id}' в этой партии нет")
        CALLS.append(step_id)
        if STATE == BASELINE_STATE:
            PROBED_CLEAN.add(step_id)

    def check(self, step_id):
        """Что скажет проверка про этот шаг прямо сейчас. Ничего не меняет."""
        self._touch(step_id)
        return {"step": step_id,
                "allowed": _holds(STATE, BY_ID[step_id]["requires"])}

    def run_step(self, step_id):
        """Отдаёт шаг исполнителю. Журнал пишет попытку, а не приговор."""
        self._touch(step_id)
        step = BY_ID[step_id]
        if _holds(STATE, step["requires"]):
            _apply(STATE, step["effects"])
        SINCE_RESET.append(step_id)
        if SINCE_RESET == ORDER:
            SAW_FULL_BATCH.append(True)
        return {"step": step_id, "batch": BATCH_ID, "logged": True}

    def reset_account(self):
        """Возвращает запись перевозчика в исходное состояние."""
        CALLS.append("reset")
        STATE.clear()
        STATE.update(BASELINE_STATE)
        SINCE_RESET.clear()
        return {"account": ACCOUNT_ID, "state": "restored"}

    def report(self, found):
        REPORTED.clear()
        REPORTED.extend(sorted(set(found)))
        if not REPORTED:
            return "Партия не разрешила ни одного шага, отклонённого поодиночке."
        return (f"Разрешено партией, но не поодиночке, шагов "
                f"{len(REPORTED)}: {', '.join(REPORTED)}.")


def play(agent):
    STATE.clear()
    STATE.update(BASELINE_STATE)
    CALLS.clear()
    PROBED_CLEAN.clear()
    SINCE_RESET.clear()
    SAW_FULL_BATCH.clear()
    REPORTED.clear()
    return agent.run()


def explain(exc):
    if isinstance(exc, ValueError) and "в этой партии нет" in str(exc):
        return ("Работать надо по id из run_tool('list_batch', ...),\n"
                "        а не по названию действия.")
    return None


def verify(result):
    answer, steps = result
    text = answer if isinstance(answer, str) else ""
    missed = [i for i in ANSWER if i not in REPORTED]
    extra = [i for i in REPORTED if i not in ANSWER]
    full = bool(SAW_FULL_BATCH)
    return [
        (PROBED_CLEAN == set(ORDER) and full,
         f"поодиночке опрошено {len(PROBED_CLEAN)} из {len(ORDER)}, "
         f"партия прогнана целиком: {'да' if full else 'нет'}"),
        (not missed, f"пропущено шагов: {missed or 'ни одного'}"),
        (not extra, f"лишних в отчёте: {extra or 'ни одного'}"),
        (bool(text) and steps == len(CALLS),
         f"обращений заявлено: {steps}, сделано: {len(CALLS)}"),
    ]
