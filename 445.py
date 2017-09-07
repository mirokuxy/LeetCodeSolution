# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    a1, a2 = [], []

    p1 = l1
    while p1:
      a1.append(p1.val)
      p1 = p1.next

    p2 = l2
    while p2:
      a2.append(p2.val)
      p2 = p2.next

    if len(a1) < len(a2):
      a1, a2 = a2, a1

    i1, i2 = len(a1)-1, len(a2)-1
    carry = 0
    while i1 >= 0:
      _sum = a1[i1] + carry
      if i2 >= 0: _sum += a2[i2]
      a1[i1] = _sum % 10
      carry = _sum / 10
      i1, i2 = i1 -1, i2 -1

    head = ListNode(0)
    current = head
    if carry:
      node = ListNode(carry)
      current.next = node
      current = node

    for val in a1:
      node = ListNode(val)
      current.next = node
      current = node

    return head.next


        