# ──────────────────────────────────────────────────
# Problem     Python If-Else
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-19, 01:43 p.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

def conditionals(n):
    if n % 2 == 1:
        return "Weird"
    elif n % 2 == 0 and n >= 2 and n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and n >= 6 and n <= 20:
        return "Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(conditionals(n))
