class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        ls = [ str(len(s)) for s in strs ]
        prefix = ','.join(ls)
        result = prefix + '|' +  ''.join(strs)
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        str_index = s.index('|')
        prefix = s[0:str_index]
        strs = s[str_index +1:]
        
        if not prefix:
            return []
        ls = map(int, prefix.split(','))
        for i in xrange(1, len(ls)):
            ls[i] = ls[i-1] + ls[i]
        
        s = []
        s.append(strs[0: ls[0]])
        for i in xrange(0, len(ls)-1):
            s.append(strs[ls[i] : ls[i+1]])
        
        return s
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))