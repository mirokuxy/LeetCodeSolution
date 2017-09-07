# 268. Missing Number
# https://leetcode.com/problems/missing-number/description/

class Solution(object):
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    _sum = sum(nums)

    return n*(n+1)/2 - _sum