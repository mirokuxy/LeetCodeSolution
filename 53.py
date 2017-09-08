# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
      return 0

    total_sum = 0
    max_sum = None
    min_sum = 0

    for i in xrange(len(nums)):
      x = nums[i]

      total_sum += x
      period_sum = total_sum - min_sum
      max_sum = max(max_sum, period_sum) if max_sum != None else period_sum
      min_sum = min(min_sum, total_sum)

    return max_sum
