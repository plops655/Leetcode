import collections
from typing import List


class Solution:

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        # make a dict of bottom of allowed to top
        patterns = collections.defaultdict(list)
        for i in range(len(allowed)):
            pattern = allowed[i]
            btm = pattern[:2]
            tp = pattern[2]
            patterns[btm].append([i,tp])


        cache = dict()
        used = [False for i in range(len(allowed))]

        def memorize(key: List[str], val: bool) -> bool:
            cache[key] = val
            return val

        def dfs(btm: str, tp: str) -> bool:

            if [btm, tp] in cache.keys():
                return cache[[btm, tp]]

            # backtrack

            # edge case:

            if len(btm) <= 1:
                if len(tp) == 1:
                    return True
                else:
                    return dfs(tp, '')

            for info in patterns[btm]:
                i = info[0]
                top = info[1]
                if used[i]:
                    continue
                used[i] = True
                if dfs(btm[1:], tp + top):
                    return memorize([btm[1:], tp + top], True)
                used[i] = False

            return memorize([btm, tp], True)

        return dfs(bottom, '')

