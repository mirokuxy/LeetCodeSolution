# 301. Remove Invalid Parentheses
# https://leetcode.com/problems/remove-invalid-parentheses/description/

# Solution: see https://leetcode.com/problems/remove-invalid-parentheses/discuss/

PAR = ['(', ')']

def remove(s, last_i, last_j, par, ans):
  count = 0
  for i in xrange(last_i, len(s)):
    if s[i] == par[0]: count += 1
    if s[i] == par[1]: count -= 1
    if count < 0:
      for j in xrange(last_j, i+1):
        if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
          remove(s[:j] + s[j+1:], i, j, par, ans)
      return

  # forloops finishes without return, count >= 0
  if par[0] == PAR[0]:  # finishes left -> right
    remove(s[::-1], 0, 0, [par[1], par[0]], ans)
  else: # finishes right -> left
    ans.append(s[::-1])
  return

class Solution(object):
  def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    ans = []
    par = [PAR[0], PAR[1]]
    remvoe(s, 0, 0, par, ans)
    return ans

      