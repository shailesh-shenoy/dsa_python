from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m = len(heights)
        n = len(heights[0])
        atlantic = set()
        pacific = set()
        queue = deque()
        visited = set()

        def add_to_pacific(i, j):
            if (i, j) not in visited:
                visited.add((i, j))
                pacific.add((i, j))
                queue.append((i, j))

        i = 0
        for j in range(n):
            add_to_pacific(i, j)

        j = 0
        for i in range(m):
            add_to_pacific(i, j)

        while queue:
            r, c = queue.popleft()
            nb = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
            for nr, nc in nb:
                if (
                    nr in range(m)
                    and nc in range(n)
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    visited.add((nr, nc))
                    pacific.add((nr, nc))
                    queue.append((nr, nc))

        visited = set()

        def add_to_atlantic(i, j):
            if (i, j) not in visited:
                visited.add((i, j))
                atlantic.add((i, j))
                queue.append((i, j))

        j = n - 1
        for i in range(m):
            add_to_atlantic(i, j)

        i = m - 1
        for j in range(n):
            add_to_atlantic(i, j)

        while queue:
            r, c = queue.popleft()
            nb = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
            for nr, nc in nb:
                if (
                    nr in range(m)
                    and nc in range(n)
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    visited.add((nr, nc))
                    atlantic.add((nr, nc))
                    queue.append((nr, nc))
        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result
