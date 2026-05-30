# ──────────────────────────────────────────────────
# Problem     Revising the Select Query I
# Difficulty  Easy
# Subdomain   Basic Select
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-29, 11:07 p.m.
# Technique   sql-select-filter
# Time        O(N)
# Space       O(1)
# Trick       Use a standard SELECT statement with a WHERE clause combining multiple conditions using the AND operator to filter rows efficiently.
# Hint        Ensure column names match schema exactly and include the semicolon.
# ──────────────────────────────────────────────────


/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

select * from CITY where population > 100000 and CountryCode = 'USA';
