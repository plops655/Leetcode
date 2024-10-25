from collections import deque
from typing import List


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        visited = [[False for c in range(cols)] for r in range(rows)]
        q = deque()

        # scan corner pieces

        if board[0][0] == 'O':
            q.append((0, 0))
            visited[0][0] = True

        if board[0][cols - 1] == 'O':
            q.append((0, cols - 1))
            visited[0][cols - 1] = True

        if board[rows - 1][0] == 'O':
            q.append((rows - 1, 0))
            visited[rows - 1][0] = True

        if board[rows - 1][cols - 1] == 'O':
            q.append((rows - 1, cols - 1))
            visited[rows - 1][cols - 1] = True

        # scan all non-corner edge pieces
        for c in range(1, cols - 1):
            if board[0][c] == 'O' and board[0][c - 1] != 'O':
                q.append((0, c))
                visited[0][c] = True
            if board[rows - 1][c] == 'O' and board[rows - 1][c - 1] != 'O':
                q.append((rows - 1, c))
                visited[rows - 1][c] = True

        for r in range(1, rows - 1):
            if board[r][0] == 'O' and board[r - 1][0] != 'O':
                q.append((r, 0))
                visited[r][0] = True
            if board[r - 1][cols - 1] == 'O' and board[r][cols - 1] != 'O':
                q.append((r, cols - 1))
                visited[r][cols - 1] = True

        while len(q) != 0:
            r, c = q.pop()
            if r > 0:
                if not visited[r - 1][c] and board[r - 1][c] == 'O':
                    q.append((r - 1, c))
                    visited[r - 1][c] = True
            if r < rows - 1:
                if not visited[r + 1][c] and board[r + 1][c] == 'O':
                    q.append((r + 1, c))
                    visited[r + 1][c] = True
            if c > 0:
                if not visited[r][c - 1] and board[r][c - 1] == 'O':
                    q.append((r, c - 1))
                    visited[r][c - 1] = True
            if c < cols - 1:
                if not visited[r][c + 1] and board[r][c + 1] == 'O':
                    q.append((r, c + 1))
                    visited[r][c + 1] = True

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and not visited[r][c]:
                    board[r][c] = 'X'

if __name__ == '__main__':
    test = Solution()
    board=[["X","O","X"],["O","X","O"],["X","O","X"]]
    test.solve(board)
    print(board)