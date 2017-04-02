class ZigzagIterator(object):

    def update_next(self):
        self.index += 1
        while self.index < self.num and self.column >= self.L[self.index]:
            self.index += 1

        if self.index >= self.num:
            self.index = 0
            self.column += 1
            while self.index < self.num and self.column >= self.L[self.index]:
                self.index += 1
                
        
    def __init__(self, *v):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = v
        self.num = len(v)
        self.L = [len(l) for l in v]
        self.column = -1
        self.index = self.num -1

        self.update_next()

    def next(self):
        """
        :rtype: int
        """
        q = self.v[self.index]
        #print "index: ", self.index, "column: ", self.column
        value = q[self.column]
        self.update_next()
        return value

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.num
