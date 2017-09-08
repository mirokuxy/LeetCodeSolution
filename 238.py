# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
        
    n = len(nums)
    products = [1] * n
    for i in xrange(1, n):
      products[i] = products[i-1] * nums[i-1]

    product = 1
    for i in xrange(n-1, -1, -1):
      products[i] *= product
      product *= nums[i]

    return products
