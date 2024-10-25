from typing import List


class Solution:

    def validUtf8Helper(self, data: List[int], l):
        if l == len(data):
            return True

        im being dumb
        val = data[l]
        if val < 128:
            return self.validUtf8Helper(data, l+1)
        if val < 192:
            return False
        if l + 1 >= data:
            return False
        val2 = data[l + 1]
        if val < 224:
            if 128 <= val2 < 2

    def validUtf8(self, data: List[int]) -> bool:
        return self.validUtf8Helper(data, 0)