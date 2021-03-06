# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/

class Solution(object):
  def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """

    count = 0

    while n > 0:
      if n % 2 == 1: count += 1
      n /= 2

    return count
        