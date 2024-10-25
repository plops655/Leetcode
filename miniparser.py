class Solution:

    def parse_int(self, s: str, i: int) -> int:
        while i < len(s):
            if s[i] == ',' or s[i] == ']':
                return i
            i += 1
        return i

    def deserialize(self, s: str) -> NestedInteger:

        # if encounter [] we are in list. store result: NestedInteger. store current: NestedInteger and add to current
        i = 0
        if s[0] != '[':
            return NestedInteger(int(s))

        # result is a list
        queue = []
        while i < len(s):
            # logic
            if s[i] == '[':
                queue.append(NestedInteger())
                i += 1
            elif s[i] == ',':
                i = self.parse_int(s, i + 1)
            elif s[i] == ']':
                child = queue.pop()
                if len(queue) == 0:
                    return child
                current = queue.pop()
                current.add(child)
                queue.append(current)
            else:
                i = self.parse_int(s, i)