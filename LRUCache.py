"""

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


"""

#Accepted

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.myCacheKeys = []
        self.myCache = {}
        self.cacheLim = capacity

    def refresh(self, key):
        if key in self.myCache:
            self.myCacheKeys.remove(key)
            self.myCacheKeys.append(key)
        else:
            self.myCacheKeys.append(key)
            if len(self.myCacheKeys) > self.cacheLim:
                self.myCache.pop(self.myCacheKeys.pop(0), None)

    def get(self, key):
        """
        :rtype: int
        """

        if key in self.myCache:
            self.refresh(key)
            return self.myCache[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.refresh(key)
        self.myCache[key] = value
