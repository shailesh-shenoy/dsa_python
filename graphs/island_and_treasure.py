from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        if not grid or not grid[0]:
            return
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def updateDistance(i, j):
            if grid[i][j] == -1:
                return inf
            if grid[i][j] != inf:
                print(i, j, grid[i][j])
                return grid[i][j]

            if (i, j) in visited:
                return inf

            visited.add((i, j))

            nb = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            for r, c in nb:
                if r in range(m) and c in range(n):
                    grid[i][j] = min(grid[i][j], 1 + updateDistance(r, c))
            return grid[i][j]

        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    visited.remove((i, j))
                updateDistance(i, j)

    def islandsAndTreasureRecursive(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        if not grid or not grid[0]:
            return
        m = len(grid)
        n = len(grid[0])

        tr = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    tr.append((i, j))

        def dfs(i, j, visited, dist):
            if grid[i][j] == -1:
                return

            grid[i][j] = min(grid[i][j], dist)
            nb = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]

            for r, c in nb:
                if (0 <= r < m) and (0 <= c < n) and (r, c) not in visited:
                    visited.add((r, c))
                    dfs(r, c, visited, dist + 1)

        for i, j in tr:
            dist = 0
            visited = set([(i, j)])
            dfs(i, j, visited, dist)


if __name__ == "__main__":
    grid = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    s = Solution()
    s.islandsAndTreasure(grid)
    print(grid)
    # Output:
