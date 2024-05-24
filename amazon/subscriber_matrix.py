from typing import List


def find_sub_groups(sub_mat: List[str]) -> int:

    mat = []
    allowed = set(["0", "1"])
    for i, s in enumerate(sub_mat):
        row = []
        for j, c in enumerate(s):
            if c not in allowed:
                break
            row.append(c)
        if len(row) == len(s):
            mat.append(row)

    return len(sub_mat)


if __name__ == "__main__":
    print(find_sub_groups(["110", "110", "001"]))
