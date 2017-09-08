# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def _isValidBST(self, root, _min, _max):
    if _min != None and not _min < root.val:
      return False
    if _max != None and not root.val < _max:
      return False
    if root.left != None:
      if not self._isValidBST(root.left, _min, root.val):
        return False
    if root.right != None:
      if not self._isValidBST(root.right, root.val, _max):
        return False

    return True

  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root: return True
    return self._isValidBST(root, None, None)

      