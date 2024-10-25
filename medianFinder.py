class MedianFinder:

    def __init__(self):
        self.stream = []

    def binarySearch(self, num: int) -> int:

        l = 0
        h = len(self.stream) - 1

        while l <= h:
            m = l + (h - l) // 2
            if self.stream[m] == num:
                return m
            elif self.stream[m] < num:
                l = m + 1
            else:
                h = m - 1

        return l - 1

    def addNum(self, num: int) -> None:

        idx = self.binarySearch(num)
        if idx < 0:
            self.stream.insert(0, num)
        else:
            self.stream.insert(idx + 1, num)

    def findMedian(self) -> float:

        if len(self.stream) % 2 == 0:
            return (self.stream[len(self.stream) // 2 - 1] + self.stream[len(self.stream) // 2]) / 2
        return self.stream[len(self.stream) // 2]


if __name__ == '__main__':
    obj = MedianFinder()
    funcs = ["addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
    inputs = [[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

    output = []
    for f, i in zip(funcs, inputs):
        if f == 'addNum':
            obj.addNum(i[0])
            output.append(None)
        elif f == 'findMedian':
            median = obj.findMedian()
            output.append(median)

    print(output)



