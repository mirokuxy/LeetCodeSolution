# 277. Find the Celebrity
# https://leetcode.com/problems/find-the-celebrity/description/

# Solution:
#   1) for each relationship query, 
#     1.1) if a knows b, then a is not a celebrity
#     1.2) if a doesn't know b, then b is not a celebrity
#     so each query can exclude 1 person from potential celebrity,
#     and by keep querying on people not excluded, we can finally locate
#     1 last potential celebrity, with n-1 queries exact.
#   2) use another n-1 queries to check if everybody else knows this potential celebrity


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
  def findCelebrity(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0: return -1

    potential = 0
    for p in xrange(1, n):
      if knows(potential, p):
        potential = p

    for p in xrange(0, n):
      if p != potential and (knows(potential, p) or not knows(p, potential)):
        return -1

    return potential