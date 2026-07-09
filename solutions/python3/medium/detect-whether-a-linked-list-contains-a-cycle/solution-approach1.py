# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true
# Problem     Cycle Detection
# Difficulty  Medium
# Subdomain   Linked Lists
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-08, 08:19 p.m.
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

