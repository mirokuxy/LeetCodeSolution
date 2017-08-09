# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/description/

# Solution: Scan with flexible length window
#    1) find first valid window:
#       let [i,j] be a window, increment j until window covers all chars;
#       increment i until window still covers all chars but is minimum
#    2) find all remaining windows:
#       increment i by 1 so that window becomes invalid;
#       repeat 1)
#    3) repeat 2) until end of string is reached

class Solution(object):
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    if len(s) == 0 or len(t) == 0:
      return ""

    # Process target string
    is_target = [0] * 256
    target_count = 0
    for char in t:
      char_ord = ord(char)
      if not is_target[char_ord]:
        target_count += 1
      is_target[char_ord] += 1

    # find first valid window
    min_i = 0
    min_j = 0

    i, j = 0, 0
    is_first = True

    is_covered = [0] * 256
    covered_count = 0
    while j < len(s):
      # remove 1 covered char
      if not is_first:
        char_ord = ord(s[i])
        is_covered[char_ord] -= 1
        covered_count -= 1
        i += 1
      is_first = False

      # expand to next valid window
      while covered_count < target_count and j < len(s):
        char_ord = ord(s[j])
        if is_target[char_ord]:
          is_covered[char_ord] += 1
          if is_covered[char_ord] == is_target[char_ord]:
            covered_count += 1
        j += 1

      #print("before:", i, j, covered_count, target_count)

      if covered_count < target_count:  # no more valid window
        break

      # shrink to minimum valid window
      while True:
        char_ord = ord(s[i])
        if is_target[char_ord] and is_covered[char_ord] == is_target[char_ord]:
          break
        else:
          if is_target[char_ord]:
            is_covered[char_ord] -= 1
        i += 1

      #print("After:", i, j, covered_count, target_count)

      # now [i, j) is a valid window, update min window
      if (min_i ==0 and min_j == 0) or (j-i) < (min_j - min_i):
        min_i, min_j = i, j

    return s[min_i : min_j]


s = Solution()
ans = s.minWindow("a", "aa")
print(ans)
