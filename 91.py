# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/description/

# Solution: Dynamic Programming
#   let S[i,j] be substring from position i to position j
#   let D[N] be number of ways to decode string S[1,N]
#   then D[N] = D[N-2]          if S[N-2, N-2] == '0'
#               D[N-2] + D[N-1] else if S[N-1, N-2] is from [10, 26]
#               D[N-1]          otherwise

class Solution(object):
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """

    # check 0
    for i in xrange(len(s)):
      if s[i] == '0':
        if i == 0 or (s[i-1] != '1' and s[i-1] != '2'):
          return 0

    # check length
    if len(s) == 0:
      return 0

    D = [ 0 for _ in xrange(len(s))]
    D[0] = 1
    for i in xrange(1, len(s)):
      num = int(s[i-1] + s[i])
      if s[i] == '0':
        D[i] = D[i-2] if i-2 >= 0 else 1
      elif num >= 10 and num <= 26:
        D[i] = D[i-1] + (D[i-2] if i-2 >= 0 else 1)
      else:
        D[i] = D[i-1]

    return D[len(s)-1]
