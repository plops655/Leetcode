from typing import List


class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        words = {word: index for index, word in enumerate(words)}
        result = []

        for idx, word in enumerate(words):
            for j in range(len(word), -1, -1):
                left = word[:j]
                reversed_left = left[::-1]
                right = word[j:]
                reversed_right = right[::-1]
                if reversed_left in words.keys() and words[reversed_left] != idx and right == reversed_right:
                    result.append([idx, words[reversed_left]])
                if j > 0:
                    if reversed_right in words.keys() and words[reversed_right] != idx and left == reversed_left:
                        result.append([words[reversed_right], idx])

        return result

if __name__ == '__main__':
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    test = Solution()
    result = test.palindromePairs(words)
    print(result)
