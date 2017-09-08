# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/description/


class Solution(object):
  def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    ans = []

    while n:
      remainder = n % 26
      offset = remainder if remainder > 0 else 26
      ans.append(chr(ord('A') + offset -1))
      n = (n-1) / 26

    ans.reverse()
    return ''.join(ans)