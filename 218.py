# 218. The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/#/description

# Interesting Problem
# Solution:
#   See here: https://discuss.leetcode.com/topic/14987/108-ms-17-lines-body-explained/2
#   No binary search tree is necessary, heap would do

from heapq import *


class Solution(object):
  def getSkyline(self, LRH):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    skyline = []
    HR = []
    i = 0
    n = len(LRH)
    while i < n or HR:
      while i < n and (not HR or -HR[0][1] >= LRH[i][0]):
        x = LRH[i][0]
        old_h = 0 if not HR else -HR[0][0]

        while i < n and LRH[i][0] == x:
          heappush(HR, (-LRH[i][2], -LRH[i][1]))
          i += 1
        if -HR[0][0] > old_h:
          skyline.append([x, -HR[0][0]])
      while HR and (i == n or -HR[0][1] < LRH[i][0]):
        x = -HR[0][1]
        while HR and -HR[0][1] <= x:
          heappop(HR)
        skyline.append([x, -HR[0][0] if HR else 0])

    return skyline

def main():
  LRH = input()
  print Solution().getSkyline(LRH)

main()

      









