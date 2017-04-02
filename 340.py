# 340. Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/#/description

# Solution:
#  1) expand when possible
#  2) shrink until it's expandable again
#  3) repeate 1) 2) until reaches end of string (also when shrink doesn't happen)

class Solution(object):
  def init(self, s, k):
    self.s = s
    self.k = k

    self.char_map = {}
    self.left = 0
    self.right = 0
    self.max_length = 0

  def expandable(self):
    return self.right < len(self.s) and \
      (len(self.char_map) < self.k or self.s[self.right] in self.char_map)

  def expand(self):
    c = self.s[self.right]
    self.right += 1
    self.max_length = max(self.max_length, self.right - self.left)

    if c in self.char_map:
      self.char_map[c] += 1
    else:
      self.char_map[c] = 1

  def shrink(self):
    if self.left == self.right:
      return False

    while self.left < self.right:
      c = self.s[self.left]
      self.left += 1
      self.char_map[c] -= 1
      if self.char_map[c] == 0:
        del self.char_map[c]
        break
    return True

  def lengthOfLongestSubstringKDistinct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    self.init(s,k)

    while True:
      while self.expandable():
        self.expand()
      if not self.shrink():
        break

    return self.max_length


def main():
  s = raw_input().strip()
  k = int(raw_input().strip())
  print Solution().lengthOfLongestSubstringKDistinct(s,k)

#  main()





