from queue import Queue
from typing import List



class Solution:

    def traverse_chunk(self, start: int, end: int, nums: List[int]) -> int:
        """Finds the largest product from start idx to end of the current chunk inclusive"""

        largest_chunk = nums[start]
        temp_product = 1
        current_product = 1

        i = start

        while i < end and nums[i] != 0:
            current_product *= nums[i]
            largest_chunk = max(largest_chunk, current_product)
            i += 1

        if current_product == largest_chunk:
            return largest_chunk

        i = start
        temp_product = 1
        while i < end:
            temp_product *= nums[i]
            if nums[i] < 0:
                break
            i += 1

        largest_chunk = max(largest_chunk, current_product // temp_product)
        return largest_chunk

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = 0
        largest_chunk = nums[0]

        exists0 = False

        while end < len(nums):
            if nums[end] == 0:
                exists0 = True
                if start != end:
                    largest_chunk = max(self.traverse_chunk(start, end, nums), largest_chunk)
                start = end + 1
            end += 1
        if end == len(nums) and start != end:
            largest_chunk = max(self.traverse_chunk(start, len(nums), nums), largest_chunk)

        if exists0:
            largest_chunk = max(largest_chunk, 0)
        return largest_chunk

if __name__ == '__main__':
    test = Solution()
    nums = [0,-3,1,1]
    maxnum = test.maxProduct(nums)
    print(maxnum)