__author__ = 'freddie'

class LRUCache:

    class CacheItem:
        def __init__(self, key, value):
            self.previous = None
            self.next = None
            self.key = key
            self.value = value

    # @param capacity, an integer
    def __init__(self, capacity):
        self.dict = {}
        self.capacity = 1 if capacity <= 0 else capacity
        self.lru = None
        self.mru = None

    # @return an integer
    def get(self, key):
        if key is None:
            raise Exception("key can't be None")

        try:
            item = self.dict[key]
        except KeyError:
            return -1

        if item is None:
            return -1
        else:
            if self.mru != item:
                if self.lru == item:
                    self.lru = item.previous

                if item.next is not None:
                    item.next.previous = item.previous

                if item.previous is not None:
                    item.previous.next = item.next

                self.mru.previous = item
                item.previous = None
                item.next = self.mru
                self.mru = item

        return item.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key is None or value is None:
            raise Exception("key or value can't be None")

        size = len(self.dict)
        existing = self.get(key)
        if existing is None or -1:
            if size == self.capacity:
                self.evictLruItem()
            item = self.CacheItem(key, value)
            item.key = key
            item.value = value
            item.next = self.mru
            item.previous = None

            if size == 0:
                self.lru = item
            else:
                self.mru.previous = item

            self.mru = item
            self.dict[key] = item
        else:
            if existing != value:
                item = self.dict[key]
                item.value = value


    def evictLruItem(self):
        if self.lru is not None:
            try:
                del self.dict[self.lru.key]
            except:
                print("cannot delete")
            if self.lru.previous is not None:
                self.lru.previous.next = None

            self.lru = self.lru.previous

if __name__ == "__main__":
    cache = LRUCache(30)

    print(cache.get(2))
    cache.set(2, 6)
    print(cache.get(1))
    cache.set(1, 5)
    cache.set(1, 2)
    print(cache.get(1))
    print(cache.get(2))

    cache = LRUCache(10)
    print(cache.get(2))
    cache.set(2, 6)
    print(cache.get(1))
    cache.set(1, 5)
    cache.set(1, 2)
    print(cache.get(1))
    print(cache.get(2))


