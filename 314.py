# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/


# Solution:
#   1) since problem doesn't say if there will be many overlapping nodes, 
#       I'm assuming there will be many overlapping nodes,
#       and nodes from left tree always comes first in the list
#   2) the way the problem represents the binary tree means the binary tree 
#       actually has a graphical structure where we can represent each node's position with a coordinate
#   3) so just use DFS to calculate all the coordinates and then sort and combine.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

def GenerateNodesInfo(root, x, y, nodes):
  if not root: return
  nodes[(x,y)].append(root.val)
  GenerateNodesInfo(root.left, x-1, y+1, nodes)
  GenerateNodesInfo(root.right, x+1, y+1, nodes)

def cmpNodeInfo(a, b):
  a_pos, a_val = a
  b_pos, b_val = b
  return cmp(a_pos, b_pos)

class Solution(object):
  def verticalOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    nodes = defaultdict(list) # (x,y) -> []
    GenerateNodesInfo(root, 0, 0, nodes)
    nodes_list = nodes.items()
    nodes_list.sort(cmp=cmpNodeInfo)

    result = []

    col = None
    val_list = []
    for node_info in nodes_list:
      node_pos, node_val = node_info
      node_col, _ = node_pos
      if node_col != col:
        if val_list:
          result.append(val_list)
        col = node_col
        val_list = []

      val_list += node_val
    if val_list:
      result.append(val_list)

    return result




