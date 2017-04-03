# 66. Plus One
# https://leetcode.com/problems/plus-one/#/description

# Solution: 
#   Easy

# Notes:
#  1) list.reverse() : changes list, no return value

class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits.reverse()

    carry = 1
    index = 0 # list garuanteed to non-empty
    tot_len = len(digits)
    while carry != 0:
      if index == tot_len:
        digits = digits + [1]
        break
      else:
        _sum = digits[index] + carry
        digits[index] = _sum % 10
        carry = _sum / 10
        index += 1

    digits.reverse()
    return digits