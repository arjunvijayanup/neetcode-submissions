class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkMap = defaultdict(int)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                keys = [f"row_{r}_{board[r][c]}", f"col_{c}_{board[r][c]}", f"box_{r//3}_{c//3}_{board[r][c]}"]
                for key in keys:
                    checkMap[key] += 1
                    if checkMap[key] > 1:
                        return False
        
        return True
                
        
