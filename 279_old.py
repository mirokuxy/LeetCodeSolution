class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [0] * (n+1)
        for i in xrange(1,n+1):
            j = 1
            while j*j <= i:
                rest = i - j*j
                val = DP[rest] + 1
                if DP[i] == 0 or DP[i] > val:
                    DP[i] = val
                j += 1
        
        return DP[n]