# 246. Strobogrammatic Number
# https://leetcode.com/problems/strobogrammatic-number/#/description

# Solution:
#  Easy. preprocessing
# Notes:
#  *) Check mid point for odd and even number

class Solution(object):
  def isStrobogrammatic(self, num):
    """
    :type num: str
    :rtype: bool
    """
    mapping = {}
    mapping['0'] = '0'
    mapping['1'] = '1'
    mapping['6'] = '9'
    mapping['8'] = '8'
    mapping['9'] = '6'

    L = len(num)
    for i in xrange(L/2 + 1):
      j = L - 1 - i
      if num[i] in mapping and num[j] == mapping[num[i]]:
        continue
      return False
    return True

