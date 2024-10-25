from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats = sorted(reservedSeats)
        if not reservedSeats:
            return 0
        curr_row = reservedSeats[0][0] - 1
        max_families = 0
        not_allowed = set()
        # not_allowed in {0,1,2} where 0 ~ left, 1 ~ middle, 2 ~ right and in not allowed for curr_row if not allowed
        i = 0
        while i < len(reservedSeats):
            row, col = reservedSeats[i]
            row -= 1
            col -= 1
            if row == curr_row:
                if 1 <= col <= 2:
                    not_allowed.add(0)
                elif 3 <= col <= 4:
                    not_allowed.add(0)
                    not_allowed.add(1)
                elif 5 <= col <= 6:
                    not_allowed.add(1)
                    not_allowed.add(2)
                elif 7 <= col <= 8:
                    not_allowed.add(2)
                i += 1
            else:
                max_families += min(3 - len(not_allowed), 2)
                not_allowed = set()
                curr_row = row

        return max_families

if __name__ == '__main__':
    n = 3
    reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    test = Solution()
    val = test.maxNumberOfFamilies(n, reservedSeats)
    print(val)
