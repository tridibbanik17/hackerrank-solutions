# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/one-pass-removal-kth-from-end/problem?isFullScreen=true
# Problem     One-Pass Removal of k-th Node from End
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-22, 12:39 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')



#
# Complete the 'removeKthNodeFromEnd' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeKthNodeFromEnd(head, k):
    if k < 0 or head is None:
        return head

    dummy = SinglyLinkedListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    # Advance fast by (k + 1). If we run out, k is invalid (k >= n).
    for _ in range(k + 1):
        if fast.next is None:
            return head
        fast = fast.next

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
    
    

if __name__ == '__main__':
    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    k = int(input().strip())

    result = removeKthNodeFromEnd(head.head, k)

    print_singly_linked_list(result, '\n')
    print()
