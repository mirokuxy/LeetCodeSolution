# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)

    if n == 1 or nums[0] < nums[-1]:
      return nums[0]
    else:
      p = 0
      q = n-1
      while p+1 < q:
        mid = (p+q) / 2
        if nums[mid] > nums[p]:
          p = mid
        else:
          q = mid
      return nums[q]




