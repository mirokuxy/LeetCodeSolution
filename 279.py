# 279. Perfect Squares
# https://leetcode.com/problems/perfect-squares/#/description

class Solution(object):
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    DP = [0] * (n+1)
    for i in xrange(1, n+1):
      j = 1
      while j * j <= i:
        new = 1 + DP[i - j*j]
        DP[i] = new if DP[i] == 0 else min(DP[i], new)
        j += 1
    return DP[n]