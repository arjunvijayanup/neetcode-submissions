class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # Move to end of list to mark it as MRU
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) # Move to end of list to mark it as MRU before inserting
        self.cache[key] = value

        if len(self.cache) > self.capacity: # After insert, check if length of cache is greater than capacity
            self.cache.popitem(last = False) # Pop item at the beginning
        