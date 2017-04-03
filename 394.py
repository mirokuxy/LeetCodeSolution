# 394. Decode String
# https://leetcode.com/problems/decode-string/#/description

# Solution:
#  Gets inspiration from Compiler Design.
#  Construct string top-down. 
#  1) Break string into parts/components
#  2) Set syntax/semantic rules for each component.
#  3) Read each component separately.

import collections

class Solution(object):
  def readPureString(self, queue):
    s = []
    while True:
      if len(queue) == 0: break
      c = queue.popleft()
      if c.isalpha():
        s.append(c)
      else:
        queue.appendleft(c)
        break  
    return ''.join(s)

  def readPureDigits(self, queue):
    s = []
    while True:
      if len(queue) == 0: break
      c = queue.popleft()
      if c.isdigit():
        s.append(c)
      else:
        queue.appendleft(c)
        break
    digits = ''.join(s)
    return long(digits)

  def readRepeat(self, queue):
    repeat = self.readPureDigits(queue)
    queue.popleft() # '['
    s = self.readString(queue)
    queue.popleft() # ']'
    return s * repeat

  def readString(self, queue):
    s = []
    while True:
      if len(queue) == 0: break
      c = queue.popleft()
      if c.isdigit():
        queue.appendleft(c)
        s.append(self.readRepeat(queue))
      elif c.isalpha():
        queue.appendleft(c)
        s.append(self.readPureString(queue))
      else:
        queue.appendleft(c)
        break
    return ''.join(s)

  def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    queue = collections.deque(s)
    ans = self.readString(queue)
    return ans

def main():
  s = raw_input().strip()
  print Solution().decodeString(s)

main()

