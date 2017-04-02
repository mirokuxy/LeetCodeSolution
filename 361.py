# 361. Bomb Enemy
# https://leetcode.com/problems/bomb-enemy/#/description

"""
Solution:
  Dynamic Programming: 
  *) For each cell, calculate how many enemies it can reach:
    1) towards left
    2) towards right
    3) upwards
    4) downwards
  *) Above info for each cell can use info from adjacent cells,
      thus using sequential scanning removes redundant work.
     For each row, do a scan from left to right and a scan from right to left
     For each col, do a scan from bottom to top and a scan from top to bottom.
Time Complexity:
  4 * M * N -> O(MN)

Personal Notes:
  *) Create 2D array:
      Wrong: matrix = [ [0] * n ] * m
        This would create a list of lists which are the same object/pointer
      Correct: matrix = [ [0] * n for i in xrange(m) ]
  *) When calculate accumulative value:
      Avoid getting value from previous cell, 
      use a separate variable to store accumulative value
  *) Use naive loop instead of custom while + step to improve perfomance.
"""

class Solution(object):
  def maxKilledEnemies(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if len(grid) == 0 or len(grid[0]) == 0:
      return 0

    m = len(grid)
    n = len(grid[0])

    row = [ [0] * n for i in xrange(m) ]
    col = [ [0] * n for i in xrange(m) ]

    for i in xrange(m):
      leftwards = xrange(n-1, -1, -1)
      rightwards = xrange(0, n, 1)
      for _range in [leftwards, rightwards]:
        tot = 0
        for j in _range:
          row[i][j] += tot
          if grid[i][j] == 'W':
            tot = 0
          elif grid[i][j] == 'E':
            tot += 1
      """
      tot = 0
      for j in xrange(n-1, -1, -1):
        row[i][j] += tot
        if grid[i][j] == 'W':
          tot = 0
        elif grid[i][j] == 'E':
          tot += 1

      tot = 0
      for j in xrange(0, n, 1):
        row[i][j] += tot
        if grid[i][j] == 'W':
          tot = 0
        elif grid[i][j] == 'E':
          tot += 1
      """

    for j in xrange(n):
      upwards = xrange(m-1, -1, -1)
      downwards = xrange(0, m, 1)
      for _range in [upwards, downwards]:
        tot = 0
        for i in _range:
          col[i][j] += tot
          if grid[i][j] == 'W':
            tot = 0
          elif grid[i][j] == 'E':
            tot += 1

      """
      tot = 0
      for i in xrange(m-1, -1, -1):
        col[i][j] += tot
        if grid[i][j] == 'W':
          tot = 0
        elif grid[i][j] == 'E':
          tot += 1

      tot = 0
      for i in xrange(0, m, 1):
        col[i][j] += tot
        if grid[i][j] == 'W':
          tot = 0
        elif grid[i][j] == 'E':
          tot += 1
      """

    max_count = 0
    for i in xrange(m):
      for j in xrange(n):
        if grid[i][j] == '0':
          count = row[i][j] + col[i][j]
          max_count = max(max_count, count)

    return max_count

def main():
  grid = input()
  print Solution().maxKilledEnemies(grid)

main()



