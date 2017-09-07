# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/description/

class Solution(object):
  def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    n = len(matrix)
    if n == 0: return matrix

    last_i = n/2 -1 
    for i in xrange(last_i + 1):
      start_j = i
      last_j = n-1 -i -1
      for j in xrange(start_j, last_j + 1):
        i2, j2 = j, n-1 -i
        i3, j3 = n-1 -i, n-1 -j
        i4, j4 = n-1 -j, i

        temp = matrix[i4][j4]
        matrix[i4][j4] = matrix[i3][j3]
        matrix[i3][j3] = matrix[i2][j2]
        matrix[i2][j2] = matrix[i][j]
        matrix[i][j] = temp

    return