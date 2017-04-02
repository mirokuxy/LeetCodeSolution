class Node():
    def __init__(self, length, isFile):
        self.length = length
        self.isFile = isFile
        self.child = None
        self.sibling = None

def DFS(node):
    if node.isFile:
        return node.length
    else:
        max_len = -1
        child = node.child
        while child != None:
            L = DFS(child)
            max_len = max(L, max_len)
            child = child.sibling
        if max_len == -1:
            return -1
        else:
            return max_len + node.length + 1

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        L = len(input)
        
        topNode = Node(0, False)
        currentNodes = [None] * (L+1)
        currentNodes[0] = topNode
        currentDepth = 0
        
        files = input.split('\n')
        for file in files:
            parts = file.split('\t')
            parts_len = len(parts)
            file_name = parts[parts_len-1]
            dot_index = file_name.find('.')
            file_name_len = len(file_name)
            is_file = dot_index >= 0 and dot_index < file_name_len -1
            
            node = Node(file_name_len, is_file)
            depth = parts_len - 1 + 1
            if currentDepth < depth:
                parent = currentNodes[currentDepth]
                parent.child = node
            else:   # currentDepth >= depth
                sibling = currentNodes[depth]
                sibling.sibling = node
            currentNodes[depth] = node
            currentDepth = depth
            
        max_len = DFS(topNode)
        if max_len == -1:
            return 0
        else:
            return max_len -1
            