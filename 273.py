# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/description/

# Solution:
#   Plain straight forward

small_int_map = {
  1 : "One",
  2 : "Two",
  3 : "Three",
  4 : "Four",
  5 : "Five",
  6 : "Six",
  7 : "Seven",
  8 : "Eight",
  9 : "Nine",
  10 : "Ten",
  11 : "Eleven",
  12 : "Twelve",
  13 : "Thirteen",
  14 : "Fourteen",
  15 : "Fifteen", 
  16 : "Sixteen",
  17 : "Seventeen",
  18 : "Eighteen",
  19 : "Nineteen",
}

tens_int_map = {
  20 : "Twenty",
  30 : "Thirty",
  40 : "Forty",
  50 : "Fifty", 
  60 : "Sixty",
  70 : "Seventy",
  80 : "Eighty",
  90 : "Ninety",
}

Billion = 10 ** 9
Million = 10 ** 6
Thousand = 10 ** 3
Hundred = 10 ** 2

large_int_map = {
  Hundred : "Hundred",
  Thousand : "Thousand",
  Million : "Million",
  Billion : "Billion",
}

def wordForTens(num):
  ans = []
  if num == 0: 
    return ans
  elif num < 20:
    ans.append(small_int_map[num])
  else:
    tens = num / 10 * 10
    ans.append(tens_int_map[tens])
    unit = num % 10
    if unit > 0:
      ans.append(small_int_map[unit])
  return ans

def wordWithUnit(num, unit):
  ans = []
  if num == 0: return ans

  h = num / Hundred
  if h > 0:
    ans.append(small_int_map[h])
    ans.append(large_int_map[Hundred])
  tens = num % Hundred
  ans += wordForTens(tens)
  if unit:
    ans.append(unit)
  return ans

class Solution(object):
  def numberToWords(self, num): # num < 3 Billion
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return "Zero"
    
    ans = []

    billions = num / Billion
    num = num % Billion
    ans += wordWithUnit(billions, large_int_map[Billion])

    millions = num / Million
    num = num % Million
    ans += wordWithUnit(millions, large_int_map[Million])

    thousands = num / Thousand
    num = num % Thousand
    ans += wordWithUnit(thousands, large_int_map[Thousand])

    units = num 
    ans += wordWithUnit(units, None)

    ans = ' '.join(ans)

    return ans


        


