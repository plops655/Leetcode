from collections import defaultdict
from typing import Set


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.time = 0
        self.cache = dict()
        self.LFU_table = defaultdict(int)
        self.LRU_table = dict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.LFU_table[key] += 1
            self.LRU_table[key] = self.time
            self.time += 1
            return self.cache[key]
        return -1

    def get_LFU(self) -> Set[int]:
        LFU_val = float('inf')
        result = set()
        for key in self.LFU_table:
            if self.LFU_table[key] < LFU_val:
                LFU_val = self.LFU_table[key]

        for key in self.LFU_table:
            if self.LFU_table[key] == LFU_val:
                result.add(key)

        return result

    def get_LRU(self, LFU: Set[int]) -> int:

        LRU_val = float('inf')
        result = 0

        for key in LFU:
            if self.LRU_table[key] < LRU_val:
                LRU_val = self.LRU_table[key]
                result = key

        return result

    def put(self, key: int, value: int) -> None:

        if key not in self.cache and len(self.cache) == self.capacity:
            LFU = self.get_LFU()
            key_to_remove = self.get_LRU(LFU)
            del self.cache[key_to_remove]
            del self.LFU_table[key_to_remove]
            del self.LRU_table[key_to_remove]

        self.cache[key] = value
        self.LFU_table[key] += 1
        self.LRU_table[key] = self.time

        self.time += 1


if __name__ == '__main__':
    capacity = 2
    result = []
    cache = LFUCache(capacity)
    result.append(cache.get(2))
    result.append(cache.get(2))
    cache.put(2,6)
    result.append(cache.get(1))
    cache.put(1,5)
    cache.put(1,2)
    result.append(cache.get(1))
    result.append(cache.get(2))

    print(result)

