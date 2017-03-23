class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        self.wordsDict = dict((word,0) for word in words)
        """
        0: original words that has not been classified
        1: Concatenated word we are looking for
        """
        concatenatedWords = []
        for word in words:
            if self.cutWord(word):
                concatenatedWords.append(word)
        return concatenatedWords

    def cutWord(self, word):
        """
        Cut the word into smaller words
        """
        for i in range(1,len(word)):
            begin = word[:i]
            if begin in self.wordsDict:
                rest = word[i:]
                if (rest in self.wordsDict) or (self.cutWord(rest)):
                    self.wordsDict[word] = 1
                    return True
        return False
