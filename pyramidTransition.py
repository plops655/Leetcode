from typing import List, Set


class Solution:

    def helper(self, bottom: str, allowed: List[str], levels: List[List[int]], current_level: int, used: List[int]) -> bool:

        if current_level == len(bottom) - 1:
            return True

        result  = False
        for i in range(len(allowed)):
            pattern = allowed[i]
            # check if can add
            add = False
            if len(levels[0]) == 0:
                if pattern[0] == bottom[0] and pattern[1] == bottom[1]:
                    add = True
                else:
                    continue
            if add or (current_level == 0 and pattern[0] == bottom[len(levels[0]) - 1] and pattern[1] == bottom[len(levels[0])]):
                add = True
            if add or (current_level != 0 and levels[current_level][-1] == pattern[0]):
                add = True

            if add and not used[i]:
                empty = False
                if len(levels[current_level]) == 0:
                    empty = True
                    levels[current_level].append(pattern[0])
                levels[current_level].append(pattern[1])
                levels[current_level + 1].append(pattern[2])
                level1_len = len(levels[current_level])
                level2_len = len(levels[current_level + 1])
                next_level = current_level
                # is current_level full?
                if level1_len == len(bottom) - current_level:
                    next_level += 1
                used[i] = True
                result = result or self.helper(bottom, allowed, levels, next_level, used)
                levels[current_level].pop(level1_len - 1)
                if empty:
                    levels[current_level].pop(level1_len - 2)
                levels[current_level + 1].pop(level2_len - 1)
                used[i] = False

        return result



            # functionc call


    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        if len(allowed) < (len(bottom) * (len(bottom) - 1)) // 2:
            return False

        used = [False for i in range(len(allowed))]
        levels = [[] for i in range(len(bottom))]
        return self.helper(bottom, allowed, levels, 0, used)

if __name__ == '__main__':
    bottom = "BCD"
    allowed = ["BCC","CDE","CEA","FFF"]
    test = Solution()
    result = test.pyramidTransition(bottom, allowed)
    print(result)

