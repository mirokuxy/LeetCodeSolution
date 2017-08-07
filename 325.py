# 325. Maximum Size Subarray Sum Equals k
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

# Solution:
#   1) Let C[N] be sum of elements from position 0 to position N,
#       then any sum of any array from position i to j can be represented as
#       C[j] - C[i-1]
#   2) Calculating C takes O(n) time, finding appropriate C[j]-C[i-1] by trying all j,i
#       will take O(n^2) time, so is not feasible
#   3) If we try all j, we will need a way to find the appropriate i in O(i) time,
#       where hashmap is a good choice

class Solution(object):
  def maxSubArrayLen(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """    
    pos = { 0: -1 }
    total_sum = 0
    max_length = 0

    for i in xrange(len(nums)):
      total_sum += nums[i]
      if total_sum not in pos:
        pos[total_sum] = i
      target_sum = total_sum - k
      if target_sum in pos:
        array_length = i - pos[target_sum]
        max_length = max(max_length, array_length)

    return max_length
