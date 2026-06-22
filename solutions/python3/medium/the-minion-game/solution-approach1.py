# ──────────────────────────────────────────────────
# Problem     The Minion Game
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 10:16 p.m.
# Technique   linear-substring-counting
# Time        O(n)
# Space       O(1)
# Trick       A substring starting at index i appears n-i times, allowing O(n) calculation without generating all substrings.
# Hint        Use n-i to count occurrences of all suffixes starting at i.
# ──────────────────────────────────────────────────

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    n = len(string)
    
    for i, char in enumerate(string):
        if char in vowels:
            kevin += n - i
        else:
            stuart += n - i
    
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")
