# 388. Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/#/description

# Notes:
# "\t\tdir".split("\t") -> [ '', '', 'dir' ]

class Solution(object):
  def lengthLongestPath(self, input):
    """
    :type input: str
    :rtype: int
    """
    names = input.split('\n')

    accumulative_length = [ 0 ] * len(names)

    def GetDepthAndName(s):
      res = s.split('\t')
      depth = len(res) - 1
      name = res[-1]
      return depth, name

    def IsFile(name):
      res = name.split('.')
      return len(res) > 1

    def SetAccumulativeLength(depth, name):
      if depth == 0:
        accumulative_length[depth] = len(name)
      else:
        accumulative_length[depth] = accumulative_length[depth-1] + len(name) + 1

    max_length = 0

    for raw_name in names:
      depth, name = GetDepthAndName(raw_name)
      SetAccumulativeLength(depth, name)
      if IsFile(name):
          max_length = max(max_length, accumulative_length[depth])

    return max_length









