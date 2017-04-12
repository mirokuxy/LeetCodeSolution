# 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/#/description

# Interesting Problem
# Solution:
#   *) Sort descending with height, then can naturally insert.
# Notes:
#   *) people with same height need to be sorted by k ascending

class Solution(object):
  def reconstructQueue(self, people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people.sort(key = lambda (h,k) : (-h, k))
    ans = []
    for p in people:
      ans.insert(p[1], p)
    return ans

