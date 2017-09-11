# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/

from collections import defaultdict

class TrieNode(object):
  def __init__(self):
    self.children = defaultdict(TrieNode)
    self.is_word = False

class Trie(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = TrieNode()

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    current = self.root
    for letter in word:
      current = current.children[letter]
    current.is_word = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    current = self.root
    for letter in word:
      if letter not in current.children:
        return False
      current = current.children[letter]
    return current.is_word

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    current = self.root
    for letter in prefix:
      if letter not in current.children:
        return False
      current = current.children[letter]
    return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)