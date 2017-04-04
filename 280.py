# 280. Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/#/description

class Solution(object):
  def wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def switch(i,j):
      nums[i], nums[j] = nums[j], nums[i]

    for i in xrange(len(nums)-1):
      j = i+1
      if i % 2 == 0 and nums[i] > nums[j]:
        switch(i,j)
      elif i % 2 == 1 and nums[i] < nums[j]:
        switch(i,j)
      