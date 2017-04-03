class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower-1] + nums + [upper+1]
        result = []
        for i in xrange(1, len(nums)):
            start = nums[i-1] +1
            end = nums[i] -1
            if start < end:
                result.append("{0}->{1}".format(start,end))
            elif start == end:
                result.append("{0}".format(start))
            else:
                pass
            
        return result
            
        