# 257. Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/description/

# Solution: straight forward DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def DFS(nodes, root, paths):
  nodes.append(str(root.val))

  # if leaf
  if not root.left and not root.right:
    path = "->".join(nodes)
    paths.append(path)
  else:
    if root.left:
      DFS(nodes, root.left, paths)
    if root.right:
      DFS(nodes, root.right, paths)

  nodes.pop()

class Solution(object):
  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
      return []

    paths = []
    nodes = []
    DFS(nodes, root, paths)

    return paths
      