# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    tmp = ListNode(0)
    tmp.next = head
    head = tmp

    prev = head
    p1 = head.next
    while True:
      if not p1:
        prev.next = None
        break

      p2 = p1.next
      if not p2:
        prev.next = p1
        break
      else:
        p3 = p2.next
        prev.next = p2
        p2.next = p1

        prev = p1
        p1 = p3

    return head.next