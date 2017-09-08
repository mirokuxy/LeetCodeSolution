# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

# Using Divide and Conquer, still can make it O(n)

class Solution(object):
  def getArrayInfo(self, nums, p, q):
    if p+1 == q:
      return nums[p], nums[p], nums[p], nums[p]

    mid = (p+q) /2
    sum1, left1, right1, mid1 = self.getArrayInfo(nums, p, mid)
    sum2, left2, right2, mid2 = self.getArrayInfo(nums, mid, q)

    _sum = sum1 + sum2
    _left = max(left1, sum1 + left2)
    _right = max(right2, sum2 + right1)
    _mid = max(mid1, mid2, right1 + left2)

    return _sum, _left, _right, _mid

  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
      return 0

    _sum, _left, _right, _mid = self.getArrayInfo(nums, 0, len(nums))

    return _mid

