from typing import List


class Solution:

    # returns idx where we can insert num into intervals
    def binarySearchInsert(self, startIntervals: List[int], endIntervals: List[int], start: int, end: int, l: int,
                           h: int) -> None:

        if h > l:
            m = l + (h - l) // 2
            if startIntervals[m] == start:
                startIntervals.insert(m, start)
                endIntervals.insert(m, end)
            elif startIntervals[m] < start:
                self.binarySearchInsert(startIntervals, endIntervals, start, end, m + 1, h)

            else:
                self.binarySearchInsert(startIntervals, endIntervals, start, end, l, m)
        else:
            if startIntervals[l] <= start:
                startIntervals.insert(l + 1, start)
                endIntervals.insert(l + 1, end)
            else:
                startIntervals.insert(l, start)
                endIntervals.insert(l, end)

    def merge(self, idxs: List[int], intervals: List[int], l: int, m: int, h: int):
        n1 = m - l + 1
        n2 = h - m
        L = [0] * (m - l + 1)
        R = [0] * (h - m)

        for i in range(n1):
            L[i] = intervals[l + i]

        for j in range(n2):
            R[j] = intervals[m + 1 + j]

        i = 0
        j = 0
        ct = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                intervals[ct] = L[i]
                idxs[ct] = l + i
                i += 1
            else:
                intervals[ct] = R[j]
                idxs[ct] = m + 1 + j
                j += 1
            ct += 1

        while i < n1:
            intervals[ct] = L[i]
            idxs[ct] = l + i
            i += 1
            ct += 1

        while j < n2:
            intervals[ct] = R[j]
            idxs[ct] = m + 1 + j
            j += 1
            ct += 1

    def sortIdxs(self, idxs: List[int], intervals: List[int], l: int, h: int):
        if l < h:
            m = l + (h - l) // 2
            self.sortIdxs(idxs, intervals, l, m)
            self.sortIdxs(idxs, intervals, m + 1, h)
            self.merge(idxs, intervals, l, m, h)

    def mergeIntervals(self, startIntervals: List[int], endIntervals: List[int]):

        startOut = []
        endOut = []

        startPtr = endPtr = 0

        while startPtr < len(startIntervals) and endPtr < len(endIntervals):
            maxEndPtr = endIntervals[endPtr]
            minStartPtr = startIntervals[startPtr]
            while startPtr < len(startIntervals) and startIntervals[startPtr] <= maxEndPtr:
                maxEndPtr = max(maxEndPtr, endIntervals[startPtr])
                startPtr += 1
            startOut.append(minStartPtr)
            endOut.append(maxEndPtr)
            endPtr = max(startPtr, endPtr + 1)

        return startOut, endOut

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        startIntervals = [i[0] for i in intervals]
        endIntervals = [i[1] for i in intervals]
        idxs = [i for i in range(len(intervals))]
        self.sortIdxs(idxs, startIntervals, 0, len(intervals) - 1)
        newEndIntervals = [endIntervals[i] for i in idxs]
        endIntervals = newEndIntervals

        start = newInterval[0]
        end = newInterval[1]

        self.binarySearchInsert(startIntervals, endIntervals, start, end, 0, len(startIntervals) - 1)
        startIntervals, endIntervals = self.mergeIntervals(startIntervals, endIntervals)

        result = [[x, y] for x, y in zip(startIntervals, endIntervals)]
        return result

if __name__ == '__main__':
    intervals = [[1,5]]
    newInterval = [2, 3]
    test = Solution()
    answer = test.insert(intervals, newInterval)
    print(answer)