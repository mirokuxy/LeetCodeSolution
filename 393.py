# 393. UTF-8 Validation
# https://leetcode.com/problems/utf-8-validation/#/description

# Notes:
#  *) convert 2-base string to int:  int('110', 2) -> 6
#  *) Always check "index out of range" in while loop

def getLen(x):
  if x & int('10000000', 2) == int('00000000', 2):
    return 1
  if x & int('11100000', 2) == int('11000000', 2):
    return 2
  if x & int('11110000', 2) == int('11100000', 2):
    return 3
  if x & int('11111000', 2) == int('11110000', 2):
    return 4
  return 0

def isTail(x):
  if x & int('11000000', 2) == int('10000000', 2):
    return True
  return False

class Solution(object):
  def validUtf8(self, data):
    """
    :type data: List[int]
    :rtype: bool
    """
    i = 0
    while i < len(data):
      x = data[i]
      _len = getLen(x)
      if _len == 0:
        return False
      else:
        end = i + _len
        i += 1
        while i < end:
          if i >= len(data) or not isTail(data[i]):
            return False
          i += 1
    return True

      








