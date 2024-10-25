from typing import List


class Solution:

    def mergeHelper(self, citations: List[int], l: int, m: int, h: int) -> None:
        L = [0] * (m - l + 1)
        H = [0] * (h - m)

        for i in range(m - l + 1):
            L[i] = citations[l + i]
        for j in range(h - m):
            H[j] = citations[m + 1 + j]

        i = j = 0

        idx = l
        while i < len(L) and j < len(H):
            if L[i] > H[j]:
                citations[idx] = L[i]
                i += 1
            else:
                citations[idx] = H[j]
                j += 1
            idx += 1

        while i < len(L):
            citations[idx] = L[i]
            i += 1
            idx += 1

        while j < len(H):
            citations[idx] = H[j]
            j += 1
            idx += 1

    def mergeSort(self, citations: List[int], l: int, h: int) -> None:

        if l < h:
            m = l + (h - l) // 2
            self.mergeSort(citations, l, m)
            self.mergeSort(citations, m + 1, h)
            self.mergeHelper(citations, l, m, h)

    def hIndex(self, citations: List[int]) -> int:
        self.mergeSort(citations, 0, len(citations) - 1)

        if citations[0] == 0:
            return 0

        if len(citations) == 1:
            return 1

        for i in range(len(citations) - 1):
            if citations[i] >= i + 1 and citations[i + 1] < i + 2:
                return i + 1

        return len(citations)
