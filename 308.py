# 308. Range Sum Query 2D - Mutable
# https://leetcode.com/problems/range-sum-query-2d-mutable/description/

class BIT2D(object):
  def __init__(self, matrix): # Assume each row has same length
    self.max_x = len(matrix)
    self.max_y = len(matrix[0]) if self.max_x > 0 else 0
    self.tree = [ [0] * (self.max_y+1) for i in xrange(self.max_x +1) ]

    # O(m,n) initialization
    col_sum = [ [0] * (self.max_y+1) for i in xrange(self.max_x+1) ]
    for x in xrange(1, self.max_x+1):
      for y in xrange(1, self.max_y+1):
        col_sum[x][y] += matrix[x-1][y-1]
        self.tree[x][y] += col_sum[x][y]
        #self.tree[x][y] += matrix[x-1][y-1]
        xx = x + (x & -x)
        yy = y + (y & -y)
        if xx <= self.max_x:
          #self.tree[xx][y] += self.tree[x][y]
          col_sum[xx][y] += col_sum[x][y]
        if yy <= self.max_y:
          self.tree[x][yy] += self.tree[x][y]
    print(self.tree)
  def cumulative(self, x, y):
    ans = 0
    while x > 0:
      yy = y
      while yy > 0:
        ans += self.tree[x][yy]
        yy -= (yy & -yy)
      x -= (x & -x)
    return ans
  def range(self, x1, y1, x2, y2):
    a = self.cumulative(x2, y2)
    b = self.cumulative(x1-1, y1-1)
    c = self.cumulative(x1-1, y2)
    d = self.cumulative(x2, y1-1)
    return a + b - c -d
  # single: can probably avoid using range, and use less time instead
  # but haven't figured out a proper way yet.
  def single(self, x, y):
    return self.range(x,y,x,y)
  def update(self, x, y, diff):
    while x <= self.max_x:
      yy = y
      while yy <= self.max_y:
        self.tree[x][yy] += diff
        yy += (yy & -yy)
      x += (x & -x)


class NumMatrix(object):

  def __init__(self, matrix):
    """
    :type matrix: List[List[int]]
    """
    self.bit = BIT2D(matrix)

  def update(self, row, col, val):
    """
    :type row: int
    :type col: int
    :type val: int
    :rtype: void
    """
    row, col = row+1, col+1

    old_val = self.bit.single(row, col)
    diff = val - old_val
    self.bit.update(row, col, diff)

  def sumRegion(self, row1, col1, row2, col2):
    """
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    row1, col1, row2, col2 = row1 +1, col1 +1, row2 +1, col2 + 1
    return self.bit.range(row1, col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)