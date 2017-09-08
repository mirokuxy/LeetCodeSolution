# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
  # @param root, a tree link node
  # @return nothing
  def connect(self, root):
    if not root: return

    head = root
    while head:
      next_head = TreeLinkNode(0)
      next_tail = next_head
      while head:
        if head.left:
          next_tail.next = head.left
          next_tail = next_tail.next
        if head.right:
          next_tail.next = head.right
          next_tail = next_tail.next
        head = head.next
      head = next_head.next




