def DFS(grid, mark, r, c, i, j):
    if not (0 <= i and i < r):
        return
    if not (0 <= j and j < c):
        return
    if grid[i][j] == '0':
        return
    if mark[i][j] == True:
        return
    mark[i][j] = True
    DFS(grid, mark, r, c, i,j-1)
    DFS(grid, mark, r, c, i,j+1)
    DFS(grid, mark, r, c, i-1,j)
    DFS(grid, mark, r, c, i+1,j)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r = len(grid)
        if r == 0:
            return 0
        c = len(grid[0])
        if c == 0:
            return 0
        
        mark = [ [False] * c for i in xrange(r) ]
        count = 0
        for i in xrange(r):
            for j in xrange(c):
                if grid[i][j] == '1' and mark[i][j] == False:
                    count += 1
                    DFS(grid, mark, r, c, i, j)
        
        return count
        
        