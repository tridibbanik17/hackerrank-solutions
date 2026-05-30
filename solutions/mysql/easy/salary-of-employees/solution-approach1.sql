-- ──────────────────────────────────────────────────
-- Problem     Employee Salaries
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    mysql
-- Status      Accepted
-- Submitted   2026-05-29, 11:22 p.m.
-- ──────────────────────────────────────────────────

/*
Enter your query here.
*/

select name from Employee where salary > 2000 and months < 10 order by employee_id;
