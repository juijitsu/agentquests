-- Level 04 · reference. Freshness is computed within a lane, not across the table.

SELECT lane, price
FROM rates
WHERE quoted_at = (SELECT MAX(quoted_at) FROM rates AS latest WHERE latest.lane = rates.lane);
