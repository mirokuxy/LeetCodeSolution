# 418. Sentence Screen Fitting
# https://leetcode.com/problems/sentence-screen-fitting/#/description

# Solution:
#  preprocess, when each word servers as the start word:
#   *) the total number of words in a line
#   *) the ending word (or next word)
#   *) the total length
#  Each such preprocess can use result from the previous preprocess,
#   conceptually thinking a line of words as a FIFO queue.
# Time Complexity:
#  For each preprocess: at most (cols / (len(word)+1))
#  Since every preprocess is using result from previous preprocess,
#  total complexity is far less than len(sentence) * (cols / (len(word)+1)),
#   which is at most : 100 * (20000 / 2) = 10^6 

# Notes:
#  *) Naively trying to simulate adding one word at a time would time-out,
#     since the total number of words the screen can fit is approximately
#      rows * cols / (len(word)+1)
#     which can be as large as 20000 * 20000 / 2 = 2 * 10^8

class Record(object):
  def __init__(self, start, end, count, length):
    self.start = start
    self.end = end
    self.count = count
    self.length = length
  def copy(self):
    return Record(self.start, self.end, self.count, self.length)

def next(i, n):
  return (i+1) % n

class Solution(object):
  def wordsTyping(self, sentence, rows, cols):
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """

    lens = [ len(word) for word in sentence ]
    tot = len(lens)

    records = [None] * tot

    record = Record(0, 0, 0, 0)
    for start in xrange(tot):
      record = record.copy()
      if start != 0:
        record.length -= lens[start-1]
        if record.length > 0:
          record.length -= 1
        record.count -= 1
        record.start = start

      while True:
        space = 1 if record.length != 0 else 0
        length = record.length + space + lens[record.end]
        if length > cols:
          break
        record.length = length
        record.count += 1
        record.end = next(record.end,tot)

      records[start] = record

    tot_count = 0
    start = 0
    for row in xrange(rows):
      record = records[start]
      tot_count += record.count
      start = record.end

    return tot_count / tot

def main():
  rows = int(raw_input().strip())
  cols = int(raw_input().strip())
  sentence = input()
  print Solution().wordsTyping(sentence, rows, cols)

#main()