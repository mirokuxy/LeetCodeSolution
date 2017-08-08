def DFS(s, p, ls, lp, i, j):
    if j == lp and i == ls:
        return True
    if j == lp:
        return False
    
    if i == ls:
        if j+1 < lp and p[j+1] == '*':
            return DFS(s, p, ls, lp, i, j+2)
        return False
        
    if p[j] != '.':
        if j+1 < lp and p[j+1] == '*':
            if DFS(s, p, ls, lp, i, j+2):
                return True
            if p[j] != s[i]:
                return False
                
            k = i
            while k < ls and s[k] == s[i]:
                if DFS(s, p, ls, lp, k+1, j+2):
                    return True
                k += 1
            return False
        else:
            if p[j] == s[i]:
                return DFS(s, p, ls, lp, i+1, j+1)
            else:
                return False
    else:   # p[j] == '.'
        if j+1 < lp and p[j+1] == '*':
            for k in xrange(i, ls+1):
                if DFS(s, p, ls, lp, k, j+2):
                    return True
            return False
        else:
            return DFS(s, p, ls, lp, i+1, j+1)


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        return DFS(s, p, ls, lp, 0, 0)
        