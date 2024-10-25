from typing import List


class Solution:

    def findMinVal(self, nums: List[int], l: int, h: int) -> int:
        if h - l + 1 == 1:
            return nums[l]
        if h - l + 1 <= 2:
            return min(nums[l], nums[h])
        m = l + (h - l) // 2
        if nums[l] >= nums[h] and nums[m] >= nums[h]:
            return self.findMinVal(nums, m, h)
        if nums[l] >= nums[h] >= nums[m]:
            return self.findMinVal(nums, l, m)
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        return self.findMinVal(nums, l, h)

if __name__ == '__main__':
    test = Solution()
    nums = [3,4,5,1,2]
    val = test.findMin(nums)
    print(val)