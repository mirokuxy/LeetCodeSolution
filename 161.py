# 161. One Edit Distance
# https://leetcode.com/problems/one-edit-distance/description/

def isOneInsert(s, t):
  if len(s) + 1 != len(t):
    return False

  inserted = False
  i,j = 0,0
  while j < len(t):
    if i == len(s) or s[i] != t[j]:
      if inserted: 
        #print('double insert')
        return False
      else:
        inserted = True
        j += 1
    else:
      i, j = i+1, j+1

  #print(s,t, 'inserted', inserted)
  return inserted

def isOneReplace(s, t):
  if len(s) != len(t):
    return False

  replaced = False
  i,j = 0,0
  while i < len(s):
    if s[i] != t[j]:
      if replaced:
        #print('double replace')
        return False
      else:
        replaced = True
        i,j = i+1, j+1
    else:
      i,j = i+1, j+1

  #print(s,t, 'replaced', replaced)
  return replaced

class Solution(object):
  def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return isOneReplace(s,t) or isOneInsert(s,t) or isOneInsert(t,s)

s = Solution()
ans = s.isOneEditDistance('a', '')
print(ans)
      