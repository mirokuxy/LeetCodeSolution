# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/

# Solution: Easy

def binaryStringToInt(s):
  ans = 0
  for c in s:
    ans = ans * 2 + (ord(c) - ord('0'))
  return ans

def intToBinaryString(i):
  a = []
  while True:
    remainder = i % 2
    i = i / 2
    a.append(str(remainder))
    if i == 0: break
  a.reverse()
  return ''.join(a)


class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a = binaryStringToInt(a)
    b = binaryStringToInt(b)
    c = a + b
    return intToBinaryString(c)

        