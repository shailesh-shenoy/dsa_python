from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        m = len(grid)
        n = len(grid[0])

        fresh_count = 0
        rotting = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                if grid[i][j] == 1:
                    fresh_count += 1
                    continue

                rotting.append((i, j))

        time = 0
        visited = set(rotting)

        while rotting:
            if fresh_count == 0:
                return time
            time += 1
            for i in range(len(rotting)):
                print(rotting, visited)
                r, c = rotting.popleft()
                nb = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
                for r, c in nb:
                    if (
                        r in range(m)
                        and c in range(n)
                        and (grid[r][c] == 1)
                        and (r, c) not in visited
                    ):
                        # No need for visited set if you mark oranges as rotten
                        # Since the if condition will not execute once grid[r][c] is 2
                        fresh_count -= 1
                        print(fresh_count)
                        visited.add((r, c))
                        rotting.append((r, c))

        return -1
