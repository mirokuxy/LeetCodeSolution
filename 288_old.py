def getAbbr(word):
    L = len(word)
    if L > 2:
        abbr = word[0] + str(L-2) + word[L-1]
    else:
        abbr = word
    return abbr
    
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = {}
        for name in dictionary:
            abbr = getAbbr(name)
            if abbr in self.dict:
                if self.dict[abbr] != name:
                    self.dict[abbr] = 2
            else:
                self.dict[abbr] = name

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = getAbbr(word)
        if abbr in self.dict:
            if isinstance(self.dict[abbr], int):
                return False
            else:
                return self.dict[abbr] == word
        else:
            return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")