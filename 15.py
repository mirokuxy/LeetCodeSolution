# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

# Solution:
#   sort, loop 1 element, two-side scan for other 2 elements. 
#   time O(N^2)

class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = set([])

    nums.sort()
    for k in xrange(len(nums)):
      a = nums[k]
      i, j = k+1, len(nums)-1
      while i<j:
        if nums[i] + nums[j] == -a:
          res.add( (a, nums[i], nums[j]) )
          i,j = i+1, j-1
        elif nums[i] + nums[j] < -a:
          i += 1
        else:
          j -= 1

    res = [ list(t) for t in res ]
    return res
