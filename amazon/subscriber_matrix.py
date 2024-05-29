from typing import List


def find_sub_groups(subs: List[str]) -> int:
    if not subs:
        return 0
    n = len(subs)
    mat = []
    allowed = set(["1", "0"])
    for s in subs:
        if len(s) != n:
            continue
        row = []
        for c in s:
            if c != "1" and c != "0":
                break
            row.append(c)
        if len(row) == n:
            mat.append(row)

    if len(mat) != n:
        return 0

    parent = [i for i in range(n)]

    count = n

    def find(x):

        while parent[x] != x:
            x = parent[x]
        return x

    def union(x, y):
        nonlocal count
        p_x = find(x)
        p_y = find(y)
        if p_x == p_y:
            return
        parent[p_y] = p_x
        count -= 1

    for i in range(n):
        for j in range(n):
            if mat[i][j] == "1":
                union(i, j)

    return count


if __name__ == "__main__":
    print(find_sub_groups(["100", "010", "001"]))
