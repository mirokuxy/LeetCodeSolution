# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Solution: heap to store k "smallest" elements, one from each list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
  def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    h = []
    for node in lists:
      if node: h.append((node.val, node))
    heapq.heapify(h)

    head = ListNode(None)
    current = head
    while len(h) > 0:
      _, node = heapq.heappop(h)
      if node.next:
        heapq.heappush(h, (node.next.val, node.next))
      node.next = None
      current.next = node
      current = node

    head = head.next
    return head

