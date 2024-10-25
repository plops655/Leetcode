from typing import List


class Solution:

    def findHeight(self, matrix: List[List[str]], r: int, c: int):
        rows = len(matrix)
        height = 0
        while r < rows:
            if matrix[r][c] != '1':
                break
            height += 1
            r += 1
        return height

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        # Find num rows and cols

        rows = len(matrix)
        cols = len(matrix[0])

        # Store max area, dp height array, and dp visited array since can have height 0 but be visited

        maxArea = 0
        height = [[0 for i in range(cols)] for j in range(rows)]
        visited = [[False for i in range(cols)] for j in range(rows)]

        # row 0 column 0
        if matrix[0][0]:
            height[0][0] = self.findHeight(matrix, 0, 0)
            visited[0][0] = True

        # key idea: if at row r col c, already looked at all cols < c for all rows and at col c rows i < r 

        # column 0
        for r in range(1, rows):

            if not matrix[r][0]:
                continue

            if height[r - 1][0]:
                height[r][0] = height[r - 1][0] - 1
            elif not height[r][0]:
                height[r][0] = self.findHeight(matrix, r, 0)

            visited[r][0] = True

            h = height[r][0]

            if h:
                tempMaxArea = 0
                tempMinHeight = rows
                for j in range(0, cols):
                    h = self.findHeight(matrix, r, j)
                    height[r][j] = h
                    visited[r][j] = True
                    tempMinHeight = min(tempMinHeight, h)
                    tempMaxArea = max(tempMaxArea, tempMinHeight * (j + 1))

                maxArea = max(tempMaxArea, maxArea)

        # rest of columns
        for c in range(1, cols):
            if not visited[0][c]:
                height[0][c] = self.findHeight(matrix, 0, c)
                visited[0][c] = True

            for r in range(1, rows):

                if not matrix[r][c]:
                    continue

                if height[r - 1][c]:
                    height[r][c] = height[r - 1][c] - 1
                elif not visited[r][c]:
                    height[r][c] = self.findHeight(matrix, r, c)

                visited[r][c] = True
                h = height[r][c]
                if h < height[r][c - 1]:
                    continue
                elif h:
                    tempMaxArea = 0
                    tempMinHeight = rows
                    for j in range(c, cols):
                        h = self.findHeight(matrix, r, j)
                        height[r][j] = h
                        visited[r][j] = True
                        tempMinHeight = min(tempMinHeight, h)
                        tempMaxArea = max(tempMaxArea, tempMinHeight * (j - c + 1))

                    maxArea = max(tempMaxArea, maxArea)

        return maxArea

if __name__ == '__main__':
    test = Solution()
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    result = test.maximalRectangle(matrix)
    print(result)