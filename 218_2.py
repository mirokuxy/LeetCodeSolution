from heapq import *

class Solution(object):
  def getSkyline(self, LRH):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    skyline = []
    HR = []

    n = len(LRH)
    i = 0
    while i < n:
      while i < n and (not HR or -HR[0][1] >= LRH[i][0]):
        x = LRH[i][0]
        old_H = -HR[0][0] if HR else 0
        while i < n and x == LRH[i][0]:
          heappush(HR, (-LRH[i][2],-LRH[i][1]) )
          i += 1
        if old_H != -HR[0][0]:
          skyline.append([x, -HR[0][0]])
      while HR and (i == n or -HR[0][1] < LRH[i][0]):
        x = -HR[0][1]
        while HR and -HR[0][1] <= x:
          heappop(HR)
        new_H = -HR[0][0] if HR else 0
        skyline.append([x, new_H])

    return skyline
    