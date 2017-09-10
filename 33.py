# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Solution:
#  1) use binary search to find the pivot point
#  2) use binary search to locate the index in either of the two parts.

class Solution(object):
  def bsearch(self, nums, target, p, q):  # [p, q)
    if p >= q: return -1
    if p+1 == q and nums[p] != target: return -1

    mid = (p+q) / 2
    if nums[mid] < target:
      return self.bsearch(nums, target, mid+1, q)
    elif nums[mid] > target:
      return self.bsearch(nums, target, p, mid)
    else:
      return mid

  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    if n == 0:
      return -1

    if n == 1 or nums[0] < nums[-1]:
      return self.bsearch(nums, target, 0, n)
    else:
      p = 0
      q = n-1
      while p+1 < q:
        mid = (p+q) / 2
        if nums[mid] > nums[p]:
          p = mid
        else:
          q = mid
      pivot = q

      if target >= nums[0]:
        return self.bsearch(nums, target, 0, pivot)
      else:
        return self.bsearch(nums, target, pivot, n)



