# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true
# Problem     Cycle Detection
# Difficulty  Medium
# Subdomain   Linked Lists
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-09, 10:13 p.m.
# Technique   two-pointers-floyd
# Time        O(n)
# Space       O(1)
# Trick       The algorithm uses two pointers moving at different speeds to detect a cycle by checking if slow == fast.
# Hint        fast.next.next will raise AttributeError if fast.next is None.
# ──────────────────────────────────────────────────



# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    
    return 0

