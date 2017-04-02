# 425. Word Squares
# https://leetcode.com/problems/word-squares/#/description

# Solution:
#   DFS with pruning, only try words with valid prefix

# Notes:
#  *) zip(*sqaure)[index] is way faster than (square[i][index] for i in xrange(len_square))
#  *) Use collections.defaultdict(list) to construct map with default value.
#  *) objects are passed by pointer. need to make a copy before storing state

import collections

class Solution(object):
  def wordSquares(self, words):
    """
    :type words: List[str]
    :rtype: List[List[str]]
    """

    # map: prefix -> list of words
    prefix_map = collections.defaultdict(list)

    length = len(words[0]) # at least 1 word garuanteed 
    for word in words:
      for i in xrange(1, length): 
        prefix = word[:i]
        prefix_map[prefix].append(word)

    squares = []

    def DFS(square):
      current = len(square)
      if current == length:
        squares.append(square[:])
        return
      prefix = ''.join(zip(*square)[current])
      for word in prefix_map[prefix]:
        square.append(word)
        DFS(square)
        square.pop()

    for word in words:
      DFS([word])

    return squares

def main():
  l = input()
  print Solution().wordSquares(l)

#main()

