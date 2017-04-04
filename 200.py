# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/#/description

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = 0 if m == 0 else len(grid[0])
    if m == 0 or n == 0:
      return 0

    visited = [ [0] * n for i in xrange(m) ]
    def inRange(i,j):
      return 0 <= i < m and 0 <= j < n
    def DFS(i,j, ordinal):
      if not inRange(i,j) or grid[i][j] == '0' or visited[i][j]: return False
      visited[i][j] = ordinal
      for (di, dj) in [(0,1), (0,-1), (-1,0), (1,0)]:
        ti, tj = di + i, dj + j
        DFS(ti, tj, ordinal)
      return True

    ordinal = 1
    for i in xrange(m):
      for j in xrange(n):
        if DFS(i, j, ordinal):
          ordinal += 1

    return ordinal - 1
