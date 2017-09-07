# 348. Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/description/

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row = [ [0] * n for i in xrange(3) ] 
        self.col = [ [0] * n for i in xrange(3) ]
        self.down_diag = [0] * 3
        self.up_diag = [0] * 3

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.row[player][row] += 1
        self.col[player][col] += 1
        if row - col == 0:
          self.down_diag[player] += 1
        if row + col == self.n - 1:
          self.up_diag[player] += 1
        
        if self.row[player][row] == self.n:
          return player
        if self.col[player][col] == self.n:
          return player
        if self.down_diag[player] == self.n:
          return player
        if self.up_diag[player] == self.n:
          return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)