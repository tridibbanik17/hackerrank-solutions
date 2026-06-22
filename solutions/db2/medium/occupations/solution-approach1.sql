-- ──────────────────────────────────────────────────
-- Problem     Occupations
-- Difficulty  Medium
-- Subdomain   Advanced Select
-- Platform    HackerRank
-- Language    db2
-- Status      Accepted
-- Submitted   2026-06-21, 10:11 p.m.
-- Technique   row-number-pivot
-- Time        O(N log N)
-- Space       O(N)
-- Trick       Use ROW_NUMBER to create grouping keys and conditional aggregation to pivot rows into columns while handling missing values with COALESCE.
-- Hint        Use PARTITION BY to align names across rows by rank.
-- ──────────────────────────────────────────────────


/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT 
    COALESCE(MAX(CASE WHEN Occupation = 'Doctor'    THEN Name END), 'NULL') AS Doctor,
    COALESCE(MAX(CASE WHEN Occupation = 'Professor' THEN Name END), 'NULL') AS Professor,
    COALESCE(MAX(CASE WHEN Occupation = 'Singer'    THEN Name END), 'NULL') AS Singer,
    COALESCE(MAX(CASE WHEN Occupation = 'Actor'     THEN Name END), 'NULL') AS Actor
FROM (
    SELECT 
        Name, 
        Occupation,
        ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name ASC) AS rn
    FROM OCCUPATIONS
) AS ranked
GROUP BY rn
ORDER BY rn;
