# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/description/

def getSameDigits(s, i, digit):
  if i == len(s):
    return 0
  else:
    count = 0
    while i < len(s) and s[i] == digit:
      i += 1
      count += 1
    return count

def DFS(s, p, i, j):
  ls, lp = len(s), len(p)

  if j == lp:
    return i == ls
  if i > ls: 
    return False

  if j+1 < lp and p[j+1] == '*':
    if p[j] == '.':
      for k in xrange(len(s) - i + 1):
        if DFS(s, p, i+k, j+2): return True
      return False
    else:
      num_digits = getSameDigits(s, i, p[j])
      for k in xrange(num_digits+1):
        if DFS(s, p, i+k, j+2): return True
      return False
  else:
    if i < ls and (p[j] == '.' or p[j] == s[i]):
      return DFS(s, p, i+1, j+1)
    else:
      return False

class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    return DFS(s, p, 0, 0)