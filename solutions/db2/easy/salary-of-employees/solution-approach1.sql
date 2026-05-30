-- ──────────────────────────────────────────────────
-- Problem     Employee Salaries
-- Difficulty  Easy
-- Subdomain   Basic Select
-- Platform    HackerRank
-- Language    db2
-- Status      Accepted
-- Submitted   2026-05-29, 11:21 p.m.
-- Technique   conditional-row-filtering
-- Time        O(N log N)
-- Space       O(N)
-- Trick       Filter rows using multiple logical conditions in the WHERE clause before sorting by the primary key.
-- Hint        DB2 requires explicit column ordering for deterministic results.
-- ──────────────────────────────────────────────────


/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

select name from Employee where salary > 2000 and months < 10 order by employee_id;
