# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

# Solution:
#   1) problems asks we do this in-place, so instead of easy solution of 
#        using another array, we need to move elements in this array instead.
#   2) since elements at the end are all 0s, so instead of swapping other elements
#       with 0s, we just need to put other element where they belong, and append 0s afterwards.

class Solution(object):
  def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    fill = 0
    target = 0

    while target < len(nums):
      while target < len(nums) and nums[target] == 0:
        target += 1
      if target < len(nums):
        if target != fill:
          nums[fill] = nums[target]
        target += 1
        fill += 1
    while fill < len(nums):
      nums[fill] = 0
      fill += 1

    return

"""
i = input()
s = Solution()
s.moveZeroes(i)
print(i)
"""
