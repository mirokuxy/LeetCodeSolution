# 259. 3Sum Smaller
# https://leetcode.com/problems/3sum-smaller/#/description

# Solution:
#  Turn 3 sum smaller into 2 sum smaller
#  then do two-sided scanning
# Notes:
#  *) Old code is better. Scan direction matters.

class Solution(object):
  def twoSumSmaller(self, nums, target):
    i = 0
    count = 0
    #print "list:", nums
    for j in xrange(len(nums)-1, 0, -1):
      if i > j:
        i = j
      else:
        while i<j and nums[i] + nums[j] < target:
          i += 1
      inc = i
      count += inc
      #print "(%d, %d) -> %d : %d" % (i,j,inc,count)
    return count

  def threeSumSmaller(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    count = 0
    nums = sorted(nums)
    #print nums
    for k in xrange(len(nums) - 2):
      tmp = self.twoSumSmaller(nums[k+1:], target-nums[k])
      count += tmp
      #print "list:", nums[k+1:], "count:", tmp, "total:", count
    return count

def main():
  nums = input()
  target = input()
  print Solution().threeSumSmaller(nums, target)

#main()

