import math


def parse(b: int, c: int, b_str: str, c_str: str):
    r = b % c
    answer = ""
    if math.ceil(b / c) >= 3:
        return answer
    for i in range(r):
        answer = answer + math.ceil(b / c) * b_str + c_str
    for i in range(c - r):
        answer = answer + math.floor(b / c) * b_str + c_str
    return answer


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # a,0,0 -> a < 3 then a * a
        # if a, b, 0 where b > a -> roof(b / a) <= 3 then roof(b/a) * b a roof(b/a) * b a ... floor(b/a) * b a floor(b / a) a
        # with r = b (mod a) roofs and a - r floors
        # a, b, c -> a - 1, b, c and doesnt end in aa or a, b - 1, c and doesnt end in bb or a, b, c - 1 and doesnt end in cc

        if a + b + c == max(a, b, c):
            if max(a, b, c) < 3:
                if a == max(a, b, c):
                    return a * "a"
                elif b == max(a, b, c):
                    return b * "b"
                elif c == max(a, b, c):
                    return c * "c"
        elif a == 0 or b == 0 or c == 0:
            if a == 0:
                if b > c:
                    return parse(b, c, "b", "c")
                else:
                    return parse(c, b, "c", "b")
            elif b == 0:
                if a > c:
                    return parse(a, c, "a", "c")
                else:
                    return parse(c, a, "c", "a")
            elif c == 0:
                if a > b:
                    return parse(a, b, "a", "b")
                else:
                    return parse(b, a, "b", "a")
        else:
            val = self.longestDiverseString(a - 1, b, c)
            if val:
                if len(val) <= 1 or val[-2:] != "aa":
                    return val + "a"
            val = self.longestDiverseString(a, b - 1, c)
            if val:
                if len(val) <= 1 or val[-2:] != "bb":
                    return val + "b"
            val = self.longestDiverseString(a, b, c - 1)
            if val:
                if len(val) <= 1 or val[-2:] != "cc":
                    return val + "c"

        return ""

if __name__ == '__main__':
    test = Solution()
    val = test.longestDiverseString(1, 1, 7)
    print(val)