# 289. Game of Life
# https://leetcode.com/problems/game-of-life/#/description

# Solution:
#  Boring problem. Use another bit for new state.

class Solution(object):
  def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    n = len(board)
    m = 0 if n == 0 else len(board[0])

    def inRange(i,j):
      return 0 <= i < n and 0 <= j < m

    #print board

    for i in xrange(n):
      for j in xrange(m):
        count = 0
        for ni in xrange(i-1, i+2):
          for nj in xrange(j-1, j+2):
            if (ni != i or nj != j) and inRange(ni,nj):
              count += board[ni][nj] & 1
        if count == 3 or (count == 2 and board[i][j] == 1):
          board[i][j] += 2

    for i in xrange(n):
      for j in xrange(m):
        board[i][j] >>= 1

    #print board

    return

def main():
  board = input()
  Solution().gameOfLife(board)

#main()
        