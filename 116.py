# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque

class Solution:
  # @param root, a tree link node
  # @return nothing
  def connect(self, root):
    if root == None: return

    queue = deque([root])
    while queue:
      next_queue = deque([])
      while queue:
        node = queue.popleft()
        node.next = queue[0] if queue else None
        if node.left: next_queue.append(node.left)
        if node.right: next_queue.append(node.right)
      queue = next_queue

    return 
