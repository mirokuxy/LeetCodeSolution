class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = [0] * self.n
        self.tree = [0] * (self.n+1)
        for i in xrange(self.n):
            self.update(i, nums[i])
        print self.nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        i = i + 1
        while i <= self.n:
            self.tree[i] += delta
            i += (i & -i)

    def cumulative(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        a = self.cumulative(j+1)
        b = self.cumulative(i)
        
        return a - b 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)