from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # IMP
        # rowSets = [set()] * 9 creates 1 set and copies its references to each index
        rowSets = [set() for _ in range(9)]
        
        colSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                    
                if val in rowSets[i]:
                    return False
                rowSets[i].add(val)
                
                if val in colSets[j]:
                    print("Col: ", i, j, val)
                    return False
                colSets[j].add(val)

                if val in boxSets[i // 3][j // 3]:
                    print("Box: ", i, j, val)
                    return False
                boxSets[i // 3][j // 3].add(val)
        
        return True