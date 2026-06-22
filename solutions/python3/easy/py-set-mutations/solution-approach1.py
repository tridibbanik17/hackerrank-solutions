# ──────────────────────────────────────────────────
# Problem     Set Mutations
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-06-21, 10:25 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))
q = int(input())

for _ in range(q):
    op, k = input().split()
    other = set(map(int, input().split()))
    getattr(A, op)(other)

print(sum(A))
