# 281. Zigzag Iterator [follow up question: k 1d vectors]
# https://leetcode.com/problems/zigzag-iterator/#/description

# Solution:
#  Maintain a cyclic linked list of queues. For each "next" request,
#   pop val from current queue, remove queue if queue is empty, 
#   and move cursor to next queue
# Time Complexity:  total length of all queues, 
#   since for every request exactly 1 queue is processed. 

# Notes:
#  *) Check input: list length == 0

import collections

class Node(object):
  def __init__(self, queue):
    self.queue = collections.deque(queue)
    self.prev = None
    self.next = None

class ZigzagIterator(object):
  def __init__(self, v1, v2):
      """
      Initialize your data structure here.
      :type v1: List[int]
      :type v2: List[int]
      """
      self.init([v1, v2])

  def init(self, lists):
    nodes = [ Node(l) for l in lists if len(l) > 0]

    if len(nodes) == 0:
      self.current = None
      return

    for i in xrange(1, len(nodes)):
      prev = nodes[i-1]
      node = nodes[i]
      prev.next = node
      node.prev = prev

    nodes[0].prev = nodes[-1]
    nodes[-1].next = nodes[0]

    self.current = nodes[0]

  def remove(self, node):
    prev = node.prev
    next = node.next
    prev.next = next
    next.prev = prev
    self.current = next
    if self.current == node:
      self.current = None

  def hasNext(self):
    """
    :rtype: bool
    """
    return self.current != None 

  def next(self):
    """
    :rtype: int
    """
    queue = self.current.queue
    val = queue.popleft()

    if len(queue) == 0:
      if self.current.next == self.current:
        self.current = None
      else:
        prev = self.current.prev
        next = self.current.next
        prev.next = next
        next.prev = prev
        self.current = next
    else:
      self.current = self.current.next

    return val

def main():
  v1 = input()
  v2 = input()
  i, v = ZigzagIterator(v1, v2), []
  while i.hasNext(): v.append(i.next())
  print v

main()
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())