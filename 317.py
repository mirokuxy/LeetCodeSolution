# 317. Shortest Distance from All Buildings
# https://leetcode.com/problems/shortest-distance-from-all-buildings/#/description

# Solution:
#  *) For each building, calculate its distance to every other empty cell
#  *) For each cell, record how many buildings it has reached
#  *) Calculate the sum of the above distance matrices
#  *) Get the min of the above sum_matrix whose cell can reach all buildings

import collections

def getNM(grid):
  return len(grid), len(grid[0])

def inRange(x, y, n, m):
  return 0 <= x < n and 0 <= y < m

def getDistanceMatrix(grid, x, y, count):
  n,m = getNM(grid)
  matrix = [ [-1] * m for i in xrange(n) ]

  queue = collections.deque([])
  queue.append((x,y))
  matrix[x][y] = 0

  while len(queue) > 0:
    x,y = queue.popleft()
    for tx,ty in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
      if inRange(tx,ty,n,m) and matrix[tx][ty] == -1 and grid[tx][ty] == 0:
        matrix[tx][ty] = matrix[x][y] + 1
        count[tx][ty] += 1
        queue.append((tx,ty))

  return matrix

def addMatrix(origin, new):
  n,m = getNM(origin)
  for i in xrange(n):
    for j in xrange(m):
      if new[i][j] > 0:
        origin[i][j] += new[i][j]

def getMin(matrix, count, tot):
  min_dist = -1
  n,m = getNM(matrix)
  for i in xrange(n):
    for j in xrange(m):
      if count[i][j] == tot and (min_dist == -1 or min_dist > matrix[i][j]):
        min_dist = matrix[i][j]

  return min_dist

class Solution(object):
  def shortestDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    
    n = len(grid)
    m = len(grid[0]) # garuanteed at least one building

    count = [ [0] * m for i in xrange(n)]

    buildings = []
    for i in xrange(n):
      for j in xrange(m):
        if grid[i][j] == 1:
          buildings.append((i,j))

    sum_matrix = [ [0] * m for i in xrange(n) ]
    for (x,y) in buildings:
      matrix = getDistanceMatrix(grid, x,y, count)
      addMatrix(sum_matrix, matrix)

    #print sum_matrix

    return getMin(sum_matrix, count, len(buildings))

def main():
  grid = input()
  print Solution().shortestDistance(grid)

main()

    