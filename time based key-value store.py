class TimeMap:

    def __init__(self):
        self.time_dict = dict()

    def binarySearchTimes(self, key: str, timestamp: int) -> int:
        # returns list idx of [timestamp, value] with value to return. if no such idx, returns -1

        lst = [info[0] for info in self.time_dict[key]]
        l = 0
        h = len(lst) - 1
        m = l + (h - l) // 2

        while l < h:
            m = l + (h - l) // 2
            if lst[m] >= timestamp:
                h = m
            elif l == h - 1:
                if lst[h] <= timestamp:
                    return h
                return l
            else:
                l = m

        if m == 0 and lst[m] > timestamp:
            return -1

        if lst[h] <= timestamp:
            return h
        return m

    def insert(self, key: str, value: str, timestamp: int) -> None:
        if not self.time_dict.__contains__(key):
            self.time_dict[key] = [[timestamp, value]]
            return

        idx = self.binarySearchTimes(key, timestamp)
        if idx == -1:
            self.time_dict[key].insert(0, [timestamp, value])
        else:
            self.time_dict[key].insert(idx + 1, [timestamp, value])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.insert(key, value, timestamp)

    def get(self, key: str, timestamp: int) -> str:

        if not self.time_dict.__contains__(key):
            return ""

        idx = self.binarySearchTimes(key, timestamp)
        if idx == -1:
            return ""

        val = self.time_dict[key][idx][1]
        return val

if __name__ == '__main__':
    lst = []

    obj = TimeMap()
    obj.set("foo", "bar", 1)
    lst.append(obj.get("foo", 1))
    lst.append(obj.get("foo", 3))
    obj.set("foo", "bar2", 4)
    lst.append(obj.get("foo", 4))
    lst.append(obj.get("foo", 5))

    print(lst)
