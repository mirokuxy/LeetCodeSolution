# 298. Binary Tree Longest Consecutive Sequence
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/#/description

# Solution:
#  DFS: calculate 
#   1) longest consecutive path starting from current node
#   2) longest consecutive path starting from any node in the current subtree

# Notes:
# *) Always check input : None, len == 0, val == 0


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def DFS(self, root):
    root_len = 1
    root_max_len = 1

    for child in (root.left, root.right):
      if child != None:
        child_len, child_max_len = self.DFS(child)
        if root.val + 1 == child.val:
          root_len = max(root_len, 1 + child_len)
        root_max_len = max(root_max_len, child_max_len)
    
    root_max_len = max(root_max_len, root_len)

    return root_len, root_max_len 

  def longestConsecutive(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
      return 0
    else:
      _, max_len = self.DFS(root)
      return max_len

