# 288. Unique Word Abbreviation
# https://leetcode.com/problems/unique-word-abbreviation/#/description

# Notes:
#  1) Get Clear info about input
#  2) Cases in this problem:
#   2.1) dictionary has no duplicate words
#   2.2) dictionary has duplicate words
#   2.3) dictionary contains query word
#   2.4) dicitonary does not contain query word

import collections

def getAbbrev(s):
  if len(s) < 3:
    return s
  
  l = len(s)
  return s[0] + str(l-2) + s[-1]

class ValidWordAbbr(object):
  def __init__(self, dictionary):
      """
      :type dictionary: List[str]
      """
      self.dict = collections.defaultdict(set)
      for word in dictionary:
        self.dict[getAbbrev(word)].add(word)

  def isUnique(self, word):
      """
      :type word: str
      :rtype: bool
      """
      abbr = getAbbrev(word)
      s = self.dict[abbr]
      if len(s) == 0 or (len(s) == 1 and word in s):
        return True
      else:
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)