# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/description/

class Solution(object):
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    m = len(matrix)
    n = len(matrix[0]) if m != 0 else 0
    if n == 0 or m == 0: return []

    ans = []

    rounds = (min(m,n)+1) /2
    for r in xrange(rounds):
      min_row = r
      max_row = m-1 -r
      min_col = r
      max_col = n-1 -r
      if min_row == max_row:
        for j in xrange(min_col, max_col+1):
          ans.append(matrix[min_row][j])
        break
      if min_col == max_col:
        for i in xrange(min_row, max_row+1):
          ans.append(matrix[i][max_col])
        break
      # right
      for j in xrange(min_col, max_col):
        ans.append(matrix[min_row][j])
      # down
      for i in xrange(min_row, max_row):
        ans.append(matrix[i][max_col])
      # left
      for j in xrange(max_col, min_col, -1):
        ans.append(matrix[max_row][j])
      # up
      for i in xrange(max_row, min_row, -1):
        ans.append(matrix[i][min_col])

    return ans