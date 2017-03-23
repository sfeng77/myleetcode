"""

 Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = False
        self.child = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        t = self.root
        for i in range(1, len(word) + 1):
            if word[0 : i] not in t.child:
                t.child[word[0:i]] = TrieNode()
            t = t.child[word[0:i]]
        t.value = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t = self.root
        for i in range(1, len(word) + 1):
            if word[0:i] not in t.child:
                return False
            t = t.child[word[0:i]]
        return t.value


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t = self.root
        for i in range(1, len(prefix) + 1):
            if prefix[0:i] not in t.child:
                return False
            t = t.child[prefix[0:i]]
        return True
