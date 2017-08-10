class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        col = 0 if row == 0 else len(matrix[0])
        
        self.row = row
        self.col = col
        self.matrix = matrix
        
        self.tree = [ [0] * (col + 1) for i in xrange(row+1) ]
        for i in xrange(row):
            for j in xrange(col):
                self.change(i+1, j+1, matrix[i][j])
        
        #print self.tree

    def changeCol(self, row, col, change):
        while col <= self.col:
            self.tree[row][col] += change
            col += (col & -col)

    def change(self, row, col, change):
        while row <= self.row:
            self.changeCol(row, col, change)
            row += (row & -row)

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.change(row+1, col+1, delta)
        #print self.tree
        
    def cumulativeCol(self, row, col):
        res = 0
        while col > 0:
            res += self.tree[row][col]
            col -= col & -col
        return res

    def cumulative(self, row, col):
        res = 0
        while row > 0:
            res += self.cumulativeCol(row, col)
            row -= row & -row
        return res

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1 +1, col1 +1, row2 +1, col2 +1
        
        #print row1, col1, row2, col2
        
        a = self.cumulative(row2, col2)
        b = self.cumulative(row1 -1, col1 -1)
        c = self.cumulative(row2, col1 -1)
        d = self.cumulative(row1 -1, col2)
        
        #print a,b,c,d
        
        return  a + b - c - d 

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)