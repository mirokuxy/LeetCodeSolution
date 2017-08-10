# 307. Range Sum Query - Mutable
# https://leetcode.com/problems/range-sum-query-mutable/description/

# Solution: Typical BIT




class BIT(object):
  def __init__(self, maxVal):
    self.maxVal = maxVal
    self.tree = [0] * (maxVal+1)  # [0, maxVal]
    self.bitmax = self.getBitmax()
  def initWithArray(self, a): # len(a) >= maxVal
    for i in xrange(1, self.maxVal+1):
      self.tree[i] += a[i-1]
      j = i + (i & -i)
      if j <= self.maxVal:
        self.tree[j] += self.tree[i]
  def getBitmax(self):  # assume maxVal > 0
    bitmax = 1
    val = self.maxVal / 2
    while val:
      bitmax <<= 1
      val /= 2
    return bitmax
  def cumulative(self, idx):
    ans = 0
    while idx > 0:
      ans += self.tree[idx]
      idx -= (idx & -idx)
    return ans
  def single(self, idx):
    ans = self.tree[idx]
    z = idx - (idx & -idx)
    idx -= 1
    while idx > z:
      ans -= self.tree[idx]
      idx -= (idx & -idx)
    return ans
  def update(self, idx, diff):
    while idx <= self.maxVal:
      self.tree[idx] += diff
      idx += (idx & -idx)
  def scale(self, times):
    for i in xrange(self.maxVal+1):
      self.tree[i] *= times
  def findG(self, cum):
    bitmax = self.bitmax
    idx = 0
    while bitmax > 0 and idx < self.maxVal:  # idx <= self.maxVal don't forget
      mid = idx + bitmax
      if mid <= self.maxVal and self.tree[mid] <= cum:
        idx = mid
        cum -= self.tree[mid]
      bitmax >>= 1
    if cum > 0:
      return -1
    else:
      return idx


class NumArray(object):
  def __init__(self, nums):
    """
    :type nums: List[int]
    """    
    self.bit = BIT(len(nums))
    self.bit.initWithArray(nums)

  def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: void
    """
    old_val = self.bit.single(i+1)
    diff = val - old_val
    self.bit.update(i+1, diff)

  def sumRange(self, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """
    return self.bit.cumulative(j+1) - self.bit.cumulative(i)
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
