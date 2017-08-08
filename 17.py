# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Solution: Plain straight forward

class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    digit_map = {
      '0' : '0',
      '1' : '1',
      '2' : 'abc',
      '3' : 'def',
      '4' : 'ghi',
      '5' : 'jkl',
      '6' : 'mno',
      '7' : 'pqrs',
      '8' : 'tuv',
      '9' : 'wxyz',
    }

    if not digits: return []

    current = [""]

    for digit in digits:
      temp = []

      chars = digit_map[digit]
      for char in chars:
        for s in current:
          temp.append(s + char)

      current = temp

    return current
