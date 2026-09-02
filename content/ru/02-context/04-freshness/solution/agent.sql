-- Уровень 04 · эталон. Свежесть считается внутри направления, а не по таблице.

SELECT lane, price
FROM rates
WHERE quoted_at = (SELECT MAX(quoted_at) FROM rates AS latest WHERE latest.lane = rates.lane);
