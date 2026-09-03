-- Level 04 · novice. The whole history comes back, January included.
--
-- TODO: every lane has several rows, and this select returns all of them.
--       One per lane is needed — the one whose quoted_at is the latest.
--       Group by lane and take the row with the maximum date.

SELECT lane, price FROM rates;
