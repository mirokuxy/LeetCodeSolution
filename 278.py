# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/

# Solution: binary search

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def firstBadVersionInRange(p, q): # p-1 is good, q+1 is bad
  m = (p+q) / 2
  if isBadVersion(m):
    if m > p: 
      return firstBadVersionInRange(p, m-1)
    else: 
      return p
  else:
    if m < q:
      return firstBadVersionInRange(m+1, q)
    else:
      return q+1

class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    return firstBadVersionInRange(1, n)
