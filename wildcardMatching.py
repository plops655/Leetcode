from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # i is idx of s and j is idx of p
        @cache
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if i == len(s) or j == len(p):
                return False

            result = False
            if p[j] != '*':
                if p[j] == '?' or s[i] == p[j]:
                    return dfs(i + 1, j + 1)
                return False
            else:
                for k in range(i, len(s) + 1):
                    result = result or dfs(k, j + 1)

            return result

        new_p = p[0]
        for i in range(1, len(p)):
            if not (p[i] == p[i - 1] and p[i - 1] == '*'):
                new_p = new_p + p[i]

        p = new_p
        return dfs(0, 0)

if __name__ == '__main__':
    s= 'aa'
    p = '*'
