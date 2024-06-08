from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        m = len(grid)
        n = len(grid[0])
        parent = [[(i, j) for j in range(len(r))] for i, r in enumerate(grid)]
        parent = [[(i, j) for j in range(n)] for i in range(m)]
        # parent = []
        # for i, r in enumerate(grid):
        #     row = []
        #     for j in range len(r):
        #         row.append((i, j))
        #     parent.append(row)

        def union(x, y):
            print("x, y", x, y)
            p_x = find(x)
            p_y = find(y)
            print("p_x, p_y", p_x, p_y)
            if p_x == p_y:
                return 0
            parent[p_x[0]][p_x[1]] = p_y
            return 1

        def find(x):
            while x != parent[x[0]][x[1]]:
                x = parent[x[0]][x[1]]
            return x

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                x = (i, j)
                if val == "0":
                    continue
                count += 1
                r = (i, j + 1)
                r_val = True if (r[1] < n and (grid[r[0]][r[1]] == "1")) else False
                l = (i, j - 1)
                l_val = True if (l[1] >= 0 and (grid[l[0]][l[1]] == "1")) else False
                b = (i + 1, j)
                b_val = True if (b[0] < m and (grid[b[0]][b[1]] == "1")) else False
                t = (i - 1, j)
                t_val = True if (t[0] >= 0 and (grid[t[0]][t[1]] == "1")) else False

                if r_val:
                    count -= union(x, r)
                if l_val:
                    count -= union(x, l)
                if b_val:
                    count -= union(x, b)
                if t_val:
                    count -= union(x, t)

        return count
