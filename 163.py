# 163. Missing Ranges
# https://leetcode.com/problems/missing-ranges/#/description

# Solution:
#  Insert lower-1 and upper+1 into list behaving as bounds,
#  scan and find valid ranges

class Solution(object):
  def findMissingRanges(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """

    nums = [lower-1] + nums + [upper+1]

    ans = []
    for i in xrange(1, len(nums)):
      start = nums[i-1] + 1
      end = nums[i] - 1
      if start == end:
        ans.append("%d" % (start))
      elif start < end:
        ans.append("%d->%d" % (start,end))

    return ans
