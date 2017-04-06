class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        
        nums.sort()
        for i in xrange(len(nums)):
            start = i+1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + nums[i] < target:
                    res += end - start
                    start += 1
                else:
                    end -= 1
        
        return res
        