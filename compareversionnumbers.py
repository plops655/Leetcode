class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        prev_i = 0
        i = 0

        prev_j = 0
        j = 0

        # I assume the versions don't end with '.'
        ver1_str = ""
        ver2_str = ""
        while i <= len(version1) or j <= len(version2):
            while i <= len(version1):
                if i == len(version1):
                    ver1_str = version1[prev_i: i]
                    break
                elif i < len(version1) and version1[i] == '.':
                    ver1_str = version1[prev_i: i]
                    prev_i = i + 1
                    i += 1
                    break
                i += 1
            while j <= len(version2):
                if j == len(version2):
                    ver2_str = version2[prev_j: j]
                    break
                elif j < len(version2) and version2[j] == '.':
                    ver2_str = version2[prev_j: j]
                    prev_j = j + 1
                    j += 1
                    break
                j += 1

            # at this point ver1[prev_i:i] and ver2[prev_j:j] are both current revisions of ver1 and ver2 to compare
            ver1_int = int(ver1_str)
            ver2_int = int(ver2_str)

            if ver1_int < ver2_int:
                return -1
            elif ver1_int > ver2_int:
                return 1

            # if i==len(version1) must parse through version2 and compare each revision to 0 (version1). Similarly if j==len(version2)
            if i == len(version1) or j == len(version2):
                break

        while i < len(version1):
            while i <= len(version1):
                if i == len(version1):
                    ver1_str = version1[prev_i: i]
                    break
                elif i < len(version1) and version1[i] == '.':
                    ver1_str = version1[prev_i: i]
                    prev_i = i + 1
                    i += 1
                    break
                i += 1
            ver1_int = int(ver1_str)
            if ver1_int > 0:
                return 1

        while j < len(version2):
            while j <= len(version2):
                if j == len(version2):
                    ver2_str = version2[prev_j: j]
                    break
                elif j < len(version2) and version2[j] == '.':
                    ver2_str = version2[prev_j: j]
                    prev_j = j + 1
                    j += 1
                    break
                j += 1
            ver2_int = int(ver2_str)
            if ver2_int > 0:
                return -1

        return 0

if __name__ == '__main__':
    test = Solution()
    version1 = "1.0.1"
    version2 = "1"
    val = test.compareVersion(version1, version2)
    print(val)