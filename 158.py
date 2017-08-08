# 158. Read N Characters Given Read4 II - Call multiple times
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/

# Solution: Keep states.
#   * input data really got me..

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

SINGLE_READ = 4

class Solution(object):
  def __init__(self):
    self.buff = [0] * 5
    self.index = 0
    self.count = 0
  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    return_read = 0

    # Important: input buf contains unwanted chars...  not expected....
    del buf[:]
    
    while self.index < self.count and return_read < n:
      buf.append(self.buff[self.index])
      self.index += 1
      return_read += 1

    if self.index < self.count: return return_read

    to_read = n - return_read
    times = to_read / SINGLE_READ + (1 if to_read % SINGLE_READ > 0 else 0)

    for _ in xrange(times):
      self.index = 0
      self.count = read4(self.buff)

      while self.index < self.count and return_read < n:
        buf.append(self.buff[self.index])
        self.index += 1
        return_read += 1

      if self.count < SINGLE_READ or return_read == n:
        break

    return return_read

      