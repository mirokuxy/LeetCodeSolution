class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r = len(grid)
        c = 0 if r == 0 else len(grid[0])
        if r == 0 or c == 0:
            return 0
        
        row = [ [0] * c for i in xrange(r) ]
        col = [ [0] * c for i in xrange(r) ]
        
        for i in xrange(r):
            tot = 0
            for j in xrange(c):
                row[i][j] += tot
                if grid[i][j] == 'E':
                    tot += 1
                elif grid[i][j] == 'W':
                    tot = 0
            
            tot = 0
            for j in xrange(c-1, -1, -1):
                row[i][j] += tot
                if grid[i][j] == 'E':
                    tot += 1
                elif grid[i][j] == 'W':
                    tot = 0
        
        for j in xrange(c):
            tot = 0
            for i in xrange(r):
                col[i][j] += tot
                if grid[i][j] == 'E':
                    tot += 1
                elif grid[i][j] == 'W':
                    tot = 0
            
            tot = 0
            for i in xrange(r-1, -1, -1):
                col[i][j] += tot
                if grid[i][j] == 'E':
                    tot += 1
                elif grid[i][j] == 'W':
                    tot = 0
        
        res = 0
        for i in xrange(r):
            for j in xrange(c):
                if grid[i][j] == '0':
                    res = max(res, row[i][j] + col[i][j])
        
        return res