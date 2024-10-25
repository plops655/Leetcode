from typing import List, Set


class Solution:

    def gather(self, s: str, beginIdx: int, endIdx: int, gatherPalindromes: List[Set[int]]) -> None:
        currentBegin = beginIdx
        currentEnd = endIdx

        gatherPalindromes[currentEnd].add(currentEnd)

        while endIdx >= beginIdx:
            if s[endIdx] != s[beginIdx]:
                currentBegin = beginIdx + 1
                currentEnd = endIdx - 1
            beginIdx += 1
            endIdx -= 1

        while currentBegin <= currentEnd:
            gatherPalindromes[currentBegin].add(currentEnd)
            currentBegin += 1
            currentEnd -= 1

    def minCut(self, s: str) -> int:
        n = len(s)
        gatherPalindromes = [set() for i in range(n)]
        self.gather(s, 0, n - 1, gatherPalindromes)
        for i in range(n-2, -1, -1):
            self.gather(s, 0, i, gatherPalindromes)
        for i in range(1, n):
            self.gather(s, i, n - 1, gatherPalindromes)


        dp = [float('inf') for i in range(n)] + [0]
        dp[0] = 1
        for i in range(n):
            endIdxs = gatherPalindromes[i]
            for j in endIdxs:
                dp[j] = min(dp[j], dp[i - 1] + 1)
        return dp[n - 1] - 1

if __name__ == '__main__':
    test = Solution()
    s = "cdd"
    value = test.minCut(s)
    print(value)