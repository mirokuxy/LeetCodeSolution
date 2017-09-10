# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.input = []
    self.output = []
    

  def push(self, x):
    """
    Push element x to the back of queue.
    :type x: int
    :rtype: void
    """
    self.input.append(x)

  def _update_output(self):
    if not self.output:
      while self.input:
        self.output.append(self.input.pop())

  def pop(self):
    """
    Removes the element from in front of queue and returns that element.
    :rtype: int
    """
    self._update_output()
    return self.output.pop()

  def peek(self):
    """
    Get the front element.
    :rtype: int
    """
    self._update_output()
    return self.output[-1]

  def empty(self):
    """
    Returns whether the queue is empty.
    :rtype: bool
    """
    return not self.input and not self.output
      

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()