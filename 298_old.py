# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
def DFS(node, length):
    res = length
    if node.left != None:
        if node.val +1 == node.left.val:
            res = max(res, DFS(node.left, length+1))
        else:
            res = max(res, DFS(node.left, 1))
    if node.right != None:
        if node.val +1 == node.right.val:
            res = max(res, DFS(node.right, length+1))
        else:
            res = max(res, DFS(node.right, 1))
    
    return res
"""
def DFS(node):
    len_continue = 1
    len_contained = 0
    if node.left != None:
        left_len_continue, left_len_contained = DFS(node.left)
        if node.left.val - 1 == node.val :
            len_continue = max(len_continue, left_len_continue + 1)
        len_contained = max([len_contained, left_len_continue, left_len_contained]) 
        
    if node.right != None:
        right_len_continue, right_len_contained = DFS(node.right)
        if node.right.val - 1 == node.val :
            len_continue = max(len_continue, right_len_continue + 1)
        len_contained = max([len_contained, right_len_continue, right_len_contained]) 

    return len_continue, len_contained

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        len_continue, len_contained = DFS(root)
        return max(len_continue, len_contained)
        