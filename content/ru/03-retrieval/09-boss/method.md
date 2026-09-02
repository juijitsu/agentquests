# Метод · Один проход на половину

Весь поисковик — цикл по подвопросам, а внутри четыре шага в строгом порядке.

**Разложите вопрос.**

```python
for part in model.split(question):
```

**Сузьте, если есть по чему.**

```python
token = model.identifier(part)
pool = run_tool("exact", {"token": token}) if token else DOCS
```

Обозначение есть не у каждой половины: у вопроса про мост его нет, и там
корпус остаётся целым.

**Отранжируйте произведением.**

```python
key=lambda d: model.similarity(part, d["text"]) * model.freshness(d)
```

**Проверьте пол по лучшему и уходите, если не дотянул.**

```python
if best < THRESHOLD:
    selection.append(model.say_missing(part))
    continue
```

**Наберите подборку, пропуская повторы.**

```python
if any(model.same_fact(doc["text"], p["text"]) for p in picked):
    continue
```

---

Проверка на честность: **уберите по очереди каждый из пяти шагов и прогоните.**
Если ответ не изменился, этот шаг в вашем поисковике ничего не делает — и на
других данных вы получите ошибку, которую он должен был предотвратить.
