# 348. Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/description/


class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.map = [ [0] * n for i in xrange(n) ]
        

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
        self.map[row][col] = player
        
        win = True
        for j in xrange(self.n):
            if self.map[row][j] != player:
                win = False
                break
        if win: return player
        
        win = True
        for i in xrange(self.n):
            if self.map[i][col] != player:
                win = False
                break
        if win: return player
        
        if row - col == 0:
            win = True
            for i in xrange(self.n):
                if self.map[i][i] != player:
                    win = False
                    break
            if win: return player
            
        if row + col == self.n -1:
            win = True
            for i in xrange(self.n):
                if self.map[i][self.n -1 - i] != player:
                    win = False
                    break
            if win: return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)