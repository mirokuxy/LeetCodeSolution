# 419. Battleships in a Board
# https://leetcode.com/problems/battleships-in-a-board/description/

class Solution(object):
  def countBattleships(self, board):
    """
    :type board: List[List[str]]
    :rtype: int
    """

    if len(board) == 0: return 0
    m, n = len(board), len(board[0])

    count = 0
    for i in xrange(m):
      for j in xrange(n):
        if board[i][j] == 'X' and (i==0 or board[i-1][j] == '.') and (j==0 or board[i][j-1] == '.'):
          count += 1

    return count