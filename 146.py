# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/

# Solution:
#   use double linked list and hashmap.
#   double linked list: store sorted recency info and support insertion and deletion
#   hashmap: store mapping from key to linked list node. support quick find.

class DLL(object):
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None

class LRUCache(object):

  def __init__(self, cap):
    """
    :type capacity: int
    """
    self.cap = cap
    self.count = 0
    self.map = {}

    self.head = DLL(0,0)
    self.tail = DLL(0,0)
    self.head.next = self.tail
    self.tail.prev = self.head

  def _remove(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev
    node.next = None
    node.prev = None

  def _appendleft(self, node):
    head = self.head
    second = head.next
    node.prev = head
    node.next = second
    second.prev = node
    head.next = node

  def _touch(self, node):
    self._remove(node)
    self._appendleft(node)

  def get(self, key):
    """
    :type key: int
    :rtype: int
    """
    if key in self.map:
      node = self.map[key]
      self._touch(node)
      return node.val
    else:
      return -1

  def put(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: void
    """
    if key in self.map:
      node = self.map[key]
      self._touch(node)
      node.val = value
    else: # insert a new one
      if self.cap >= 1:
        if self.count >= self.cap:
          node = self.tail.prev
          self._remove(node)
          self.count -= 1
          del self.map[node.key]

        node = DLL(key, value)
        self._appendleft(node)
        self.count += 1
        self.map[key] = node
    return 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)