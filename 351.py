# 351. Android Unlock Pattern
# https://leetcode.com/problems/android-unlock-patterns/#/description

# Notes:
#  *) after n numbers are used, stop going deeper.

class Solution(object):
  def init(self, m, n):
    Rules = [ [0] * 10 for i in xrange(10) ]
    Rules[1][3] = 2
    Rules[1][7] = 4
    Rules[1][9] = 5
    Rules[2][8] = 5
    Rules[3][1] = 2
    Rules[3][7] = 5
    Rules[3][9] = 6
    Rules[4][6] = 5
    Rules[6][4] = 5
    Rules[7][1] = 4
    Rules[7][3] = 5
    Rules[7][9] = 8
    Rules[8][2] = 5
    Rules[9][1] = 5
    Rules[9][3] = 6
    Rules[9][7] = 8
    self.Rules = Rules

    self.m = m
    self.n = n
    self.count = 0
    self.visited = [ False ] * 10

  def DFS(self, last_key, depth):
    if depth > self.n:
      return

    if self.m <= depth:
      self.count += 1

    for i in xrange(1, 10):
      if not self.visited[i]:
        middle_key = self.Rules[last_key][i]
        if middle_key == 0 or self.visited[middle_key]:
          self.visited[i] = True
          self.DFS(i, depth+1)
          self.visited[i] = False

  def numberOfPatterns(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    self.init(m, n)
    for i in xrange(1, 10):
      self.visited[i] = True
      self.DFS(i, 1)
      self.visited[i] = False

    return self.count

    
