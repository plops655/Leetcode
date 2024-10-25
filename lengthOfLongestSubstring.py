class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = dict()
        max_length = 0
        start = 0
        for i in range(len(s)):
            if s[i] in characters and characters[s[i]] >= start:
                max_length = max(max_length, i - start)
                start = characters[s[i]] + 1
                characters[s[i]] = i
            else:
                characters[s[i]] = i
                # characters.add(s[i])

        return max(max_length, len(s) - start)


if __name__ == '__main__':
    test = Solution()
    s = "abba"
    result = test.lengthOfLongestSubstring(s)
    print(result)