-- ──────────────────────────────────────────────────
-- Problem     Print Prime Numbers
-- Difficulty  Medium
-- Subdomain   Alternative Queries
-- Platform    HackerRank
-- Language    sql
-- Status      Accepted
-- Submitted   2026-05-29, 11:31 p.m.
-- ──────────────────────────────────────────────────



DECLARE @Output AS VARCHAR(MAX) = '';

WITH digit(d) AS (
  SELECT 0 UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL
  SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL
  SELECT 8 UNION ALL SELECT 9
),
numbers AS (
  SELECT a.d * 100 + b.d * 10 + c.d + 1 AS n
  FROM digit a CROSS JOIN digit b CROSS JOIN digit c
)
SELECT @Output += CAST(a.n AS VARCHAR(4)) + '&'
FROM numbers a
LEFT JOIN numbers b 
  ON SQRT(a.n) >= b.n AND b.n > 1 AND a.n % b.n = 0
WHERE a.n > 1
GROUP BY a.n
HAVING SUM(CASE WHEN b.n IS NOT NULL THEN 1 ELSE 0 END) = 0
ORDER BY a.n;

PRINT SUBSTRING(@Output, 1, LEN(@Output) - 1);

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

