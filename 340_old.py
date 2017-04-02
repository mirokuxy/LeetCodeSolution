class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        if k <= 0:
            return 0
        
        dict = {}
        
        end = 0
        max_len = 0
        for start in xrange(len(s)):
            if start != 0:
                dict[s[start -1]] -= 1
                if dict[s[start -1]] == 0:
                    del dict[s[start -1]]
            while True:
                if end == len(s):
                    break
                if s[end] in dict:
                    dict[s[end]] += 1
                    end += 1
                else:
                    if len(dict) == k:
                        break
                    else:
                        dict[s[end]] = 1
                        end += 1
            max_len = max(max_len, end - start)
        
        return max_len
                