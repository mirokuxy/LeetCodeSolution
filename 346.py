# 346. Moving Average from Data Stream
# https://leetcode.com/problems/moving-average-from-data-stream/#/description

# Solution:
#  Maintain the window sum and element count as windows slides.

import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = size
        self.queue = collections.deque([])
        self.sum = 0
        self.count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.sum += val
        self.count += 1
        if len(self.queue) > self.window:
          self.sum -= self.queue.popleft()
          self.count -= 1

        return 0 if self.count == 0 else float(self.sum) / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)