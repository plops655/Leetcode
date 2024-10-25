from functools import cache
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        val_cache = dict()
        def return_cache(i, d, val):
            val_cache[(i, d)] = val
            return val

        @cache
        def dfs(i: int, d: int) -> int:

            if d == k + 1:
                if i == len(nums):
                    return 0
                return 10 ** 9 + 1
            if i == len(nums):
                return 10 ** 9 + 1

            if (i, d) in val_cache:
                return val_cache[(i, d)]

            ans = 10 ** 9 + 1
            sum_val = 0
            for a in range(i, len(nums)):
                # i -> a + dfs (a + 1 ->)
                sum_val += nums[a]
                temp = max(sum_val, dfs(a + 1, d + 1))
                ans = min(ans, temp)

            return return_cache(i, d, ans)

        return dfs(0, 1)

if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    k = 2
    test = Solution()
    result = test.splitArray(nums, k)
    print(result)


