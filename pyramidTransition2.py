from typing import List


class Solution:

    def helper(self, bottom: str, allowed: List[str], levels: List[List[int]], current_level: int, idx: int, used: List[int]) -> bool:

        if current_level == len(bottom) - 1:
            return True

        result  = False
        for i in range(len(allowed)):
            pattern = allowed[i]
            # check if can add
            add = False
            if current_level == 0:
                if pattern[0] == bottom[idx] and pattern[1] == bottom[idx + 1]:
                    add = True
            else:
                if pattern[0] == levels[current_level][idx] and pattern[1] == levels[current_level][idx + 1]:
                    add = True

            if used[i]:
                add = False

            if add:
                levels[current_level + 1].append(pattern[2])
                next_level_len = len(levels[current_level + 1])
                next_current = current_level
                # is current_level full?
                old_idx = idx
                idx += 1
                if next_level_len == len(bottom) - current_level - 1:
                    next_current += 1
                    idx = 0

                used[i] = True
                result = result or self.helper(bottom, allowed, levels, next_current, idx, used)
                levels[current_level + 1].pop(next_level_len - 1)
                used[i] = False
                idx = old_idx

        return result



            # functionc call


    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        if len(allowed) < (len(bottom) * (len(bottom) - 1)) // 2:
            return False

        used = [False for i in range(len(allowed))]
        levels = [[] for i in range(len(bottom))]
        return self.helper(bottom, allowed, levels, 0, 0, used)

if __name__ == '__main__':
    bottom = "BCD"
    allowed = ["BCC","CDE","CEA","FFF"]
    test = Solution()
    result = test.pyramidTransition(bottom, allowed)
    print(result)
