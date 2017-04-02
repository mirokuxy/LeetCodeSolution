class Record(object):
    def __init__(self, start, end, count, length):
        self.start = start
        self.end = end
        self.count = count
        self.length = length
    def copy(self):
        return Record(self.start, self.end, self.count, self.length)
    def __repr__(self):
        return "({0},{1},{2},{3})".format(self.start, self.end, self.count, self.length)
    
def next(i, n):
    return (i+1) % n

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        lens = [ len(s) for s in sentence ]
        
        record = Record(0, 0, 0, 0)
        records = []
        feasible = True
        for i in xrange(len(lens)):
            record = record.copy()
            if i != 0:
                record.length -= lens[i-1]
                if record.length > 0:
                    record.length -= 1
                record.start = i
            while True:
                if record.length == 0:
                    target_len = lens[record.end]
                else:
                    target_len = lens[record.end] + 1
                    
                if record.length + target_len <= cols:
                    record.length += target_len
                    record.end = next(record.end, len(lens))
                    if record.end == 0:
                        record.count += 1
                else: 
                    break
            
            if record.length == 0:
                feasible = False
                break
            
            records.append(record)
            
        print records
            
        if not feasible:
            return 0
        
        count = 0
        index = 0
        for row in xrange(rows):
            record = records[index]
            count += record.count
            index = record.end
        
        return count
                