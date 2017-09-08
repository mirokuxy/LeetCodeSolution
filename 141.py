# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    
    if head == None: return False
    head.val = head
    
    while True:
      if head.next == None: return False 
      if head.val.next == None: return False
      if head.val.next.next == None: return False
      
      head.next.val = head.val.next.next
      head = head.next
      if head == head.val: return True
          