from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) == d:
            return sum(jobDifficulty)

        if d == 0:
            return -1

        if d == 1:
            return max(jobDifficulty)

        dp = [[0 for j in range(d + 1)] for i in range(len(jobDifficulty) + 1)]

        # do base cases first

        for i in range(len(jobDifficulty)):
            dp[i][1] = max(jobDifficulty[i:])

        for j in range(d + 1):
            dp[len(jobDifficulty)][j] = 10 ** 6

        for j in range(2, d + 1):
            for i in range(len(jobDifficulty) - 1, -1, -1):
                ans = 10 ** 6
                for k in range(i, len(jobDifficulty)):
                    temp = max(jobDifficulty[i: k + 1]) + dp[k + 1][j - 1]
                    ans = min(ans, temp)
                dp[i][j] = ans

        return dp[0][d]



if __name__ == '__main__':
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    test = Solution()
    result = test.minDifficulty(jobDifficulty, d)
    print(result)
