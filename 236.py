# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def _LCA(self, root, p, q):
    P, Q, LCA = False, False, None

    if root.left:
      pp, qq, lca = self._LCA(root.left, p, q)
      P = P or pp
      Q = Q or qq
      LCA = LCA or lca

    if root.right:
      pp, qq, lca = self._LCA(root.right, p, q)
      P = P or pp
      Q = Q or qq
      LCA = LCA or lca

    if root == p:
      P = True
    if root == q:
      Q = True
    if not LCA and P and Q:
      LCA = root

    return P, Q, LCA

  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    P, Q, LCA = self._LCA(root, p, q)
    return LCA
     