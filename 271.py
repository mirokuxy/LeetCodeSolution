# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/#/description

# Solution:
#   Since strings can contain any character/pattern, hoping to insert
#   some special pattern between strings to distinguish them is not feasible
#   So it's necessary to have some header info the pattern of which 
#   we can control and distinguish easily.
#   Include lengths of strings in the header, 
#   and we'll be able to tell strings apart.

# Notes:
#  1) ''.split(',') -> ['']
#     '4'.split(',') -> ['4']
#     '4,'.split(',') -> ['4', '']
#  2) split -> List[str]
#  3) join  <- List[str]
#  4) Check input empty

class Codec(object):
  def encode(self, strs):
    """Encodes a list of strings to a single string.
    
    :type strs: List[str]
    :rtype: str
    """
    lens = [ str(len(s)) for s in strs ]
    prefix = ','.join(lens)
    return prefix + '|' + ''.join(strs)

  def decode(self, s):
    """Decodes a single string to a list of strings.
    
    :type s: str
    :rtype: List[str]
    """
    strs = []

    middle = s.index('|')
    prefix = s[:middle]
    content = s[middle+1:]
    
    if len(prefix) == 0:
      return strs

    lens = map(int, prefix.split(','))

    start = 0
    for i in xrange(len(lens)):
      end = start + lens[i]
      s = content[start:end]
      strs.append(s)
      start = end
    
    return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))