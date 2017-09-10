def inRange(r, c, i, j):
    return 0 <= i and i < r and 0 <= j and j < c
        
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        r = len(matrix)
        c = 0 if r == 0 else len(matrix[0])
        if r == 0 or c == 0:
            return result
        
        visited = [ [False] * c for i in xrange(r) ]
        
        
        Right = 0
        Down = 1
        Left = 2
        Up = 3
        increment = [ [0,1], [1,0], [0,-1], [-1,0] ]
        
        i = 0
        j = 0
        visited[i][j] = True
        result.append(matrix[i][j])
        
        direction = Right
        while True:
            next_i = i + increment[direction][0]
            next_j = j + increment[direction][1]
            if inRange(r,c, next_i, next_j) and not visited[next_i][next_j]:
                i = next_i
                j = next_j
                visited[i][j] = True
                result.append(matrix[i][j])
            else:
                direction = (direction +1) % 4
                next_i = i + increment[direction][0]
                next_j = j + increment[direction][1]
                if inRange(r,c, next_i, next_j) and not visited[next_i][next_j]:
                    i = next_i
                    j = next_j
                    visited[i][j] = True
                    result.append(matrix[i][j])
                else:
                    break
                
                
        return result
        
        
        
        ^^¨^