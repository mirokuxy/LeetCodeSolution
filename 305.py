# 305. Number of Islands II
# https://leetcode.com/problems/number-of-islands-ii/#/description

# Solution:
#   UnionFindSet
# Time Complexity: O( max(len(positions),m*n) )
#   UnionFindSet with "union by rank" and "path compression" optimization
#   is generally constant in time for search and merge.


class UnionFindSet(object):
  def __init__(self, n):
    self.parent = [ i for i in xrange(n+1) ]
    self.rank = [ 0 for i in xrange(n+1) ]
  def find(self, k):
    if self.parent[k] != k:
      self.parent[k] = self.find(self.parent[k])
    return self.parent[k]
  def union(self, x, y):
    px = self.find(x)
    py = self.find(y)
    if self.rank[px] < self.rank[py]:
      self.parent[px] = py
    elif self.rank[py] < self.rank[px]:
      self.parent[py] = px
    else:
      self.parent[py] = px
      self.rank[px] += 1

class Solution(object):
  def numIslands2(self, m, n, positions):
    """
    :type m: int
    :type n: int
    :type positions: List[List[int]]
    :rtype: List[int]
    """
    def inRange(x,y):
      if 0 <= x < m and 0 <= y < n:
        return True
      return False

    grid = [ [0] * n for i in xrange(m) ]
    us = UnionFindSet(m*n)

    index = 0
    count = 0
    counts = []
    for position in positions:
      x = position[0]
      y = position[1]
      index += 1
      grid[x][y] = index
      count += 1
      for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        tx, ty = dx + x, dy + y
        if inRange(tx,ty) and grid[tx][ty] > 0:
          p0 = us.find(grid[x][y])
          p1 = us.find(grid[tx][ty])
          if p0 != p1:
            us.union(p0, p1)
            count -= 1
      counts.append(count)
    return counts

















