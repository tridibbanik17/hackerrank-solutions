# ──────────────────────────────────────────────────
# Problem     Is This a Binary Search Tree?
# Difficulty  Medium
# Subdomain   Trees
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-05-26, 01:30 a.m.
# Technique   recursive-range-validation
# Time        O(N)
# Space       O(H)
# Trick       Pass down a valid range [min, max] to each recursive call to ensure every node satisfies the BST property relative to all ancestors.
# Hint        Use float('-inf') and float('inf') for initial boundary conditions.
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
        
