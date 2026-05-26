# ──────────────────────────────────────────────────
# Problem     List Comprehensions
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-25, 11:56 p.m.
# ──────────────────────────────────────────────────

def list_comprehension(x,y,z,n):
    res = []
    all_possibilities = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                all_possibilities.append([i,j,k])
                
    for element in all_possibilities:
        if (element[0]+element[1]+element[2]) != n:
            res.append([element[0],element[1],element[2]])
    return res
        

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list_comprehension(x,y,z,n))


