class Solution:
    def numDecodings(self, s: str) -> int:

        decode_dict = dict()
        for i in range(1, 27):
            decode_dict[f"{i}"] = chr(ord('A') + i - 1)

        cache = dict()
        def dfs(message: str) -> int:
            if len(message) == 0:
                return 1
            if len(message) == 1:
                if message in decode_dict:
                    return 1
            if len(message) == 2:
                rslt = 0
                if message[0] in decode_dict and message[1] in decode_dict:
                    rslt += 1
                if message in decode_dict:
                    rslt += 1
                return rslt
            val0 = message[0]
            val1 = message[:2]
            result = 0
            if val0 in decode_dict:
                result += dfs(message[1:])
            if val1 in decode_dict:
                result += dfs(message[2:])

            return result

        return dfs(s)






if __name__ == '__main__':
    test = Solution()
    string = "123123"
    result = test.numDecodings(string)
    print(result)