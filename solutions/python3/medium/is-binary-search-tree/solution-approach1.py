# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/is-binary-search-tree/problem?isFullScreen=true
# Problem     Is This a Binary Search Tree?
# Difficulty  Medium
# Subdomain   Trees
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-08, 08:14 p.m.
# Technique   recursive-range-validation
# Time        O(N)
# Space       O(H)
# Trick       The function uses recursive calls with float('-inf') and float('inf') to propagate valid data boundaries down the tree branches.
# ──────────────────────────────────────────────────



""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.data <= min_val or root.data >= max_val:
        return False
    return (check_binary_search_tree_(root.left, min_val, root.data) and
            check_binary_search_tree_(root.right, root.data, max_val))
        
