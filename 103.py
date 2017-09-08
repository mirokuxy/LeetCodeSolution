# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
  def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    if root == None: # remember input check
      return []

    queue = deque([root])
    all_nodes = []

    while queue:
      next_queue = deque([])
      nodes = []
      while queue:
        node = queue.popleft()
        nodes.append(node.val)
        if node.left: next_queue.append(node.left)
        if node.right: next_queue.append(node.right)
      all_nodes.append(nodes)
      queue = next_queue

    for i in xrange(len(all_nodes)):
      if i % 2 == 1:
        all_nodes[i].reverse()

    return all_nodes
