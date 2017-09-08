# 174. Dungeon Game
# https://leetcode.com/problems/dungeon-game/description/

# Solution: 
#  see https://leetcode.com/problems/dungeon-game/discuss/
#  direction matters

class Solution(object):
  def calculateMinimumHP(self, dungeon):
    """
    :type dungeon: List[List[int]]
    :rtype: int
    """

    n = len(dungeon)
    m = len(dungeon[0]) if n > 0 else 0
    if m == 0 or n == 0: return 0

    hp = [0] * m
    hp[m-1] = max(1- dungeon[n-1][m-1], 1)
    for j in xrange(m-2, -1, -1):
      hp[j] = max(hp[j+1] - dungeon[n-1][j], 1)

    for i in xrange(n-2, -1, -1):
      old_hp = hp
      hp = [0] * m

      hp[m-1] = max(old_hp[m-1] - dungeon[i][m-1], 1)
      for j in xrange(m-2, -1, -1):
        hp[j] = max( min(old_hp[j], hp[j+1]) - dungeon[i][j], 1)

    return hp[0]
