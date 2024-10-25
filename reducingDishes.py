from typing import List


class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        neg = []
        pos = []

        for i in satisfaction:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        neg = sorted(neg)
        pos = sorted(pos)
        sum_of_pos_values = sum(pos)

        if sum_of_pos_values == 0:
            return 0

        i = 0
        rolling_neg_sum = sum(neg)
        while i < len(neg):
            if abs(rolling_neg_sum) > sum_of_pos_values:
                rolling_neg_sum -= neg[i]
                i += 1
            else:
                break

        result = 0
        for j in range(i, len(neg)):
            result += (j - i + 1) * neg[j]

        for j in range(len(pos)):
            result += (len(neg) - i + 1 + j) * pos[j]

        return result


if __name__ == '__main__':
    satisfaction = [-1,-4,-5]
    test = Solution()
    result = test.maxSatisfaction(satisfaction)
    print(result)