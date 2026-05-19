class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checkMap = defaultdict(int)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                checkMap[f"row_{r}_{board[r][c]}"] += 1
                checkMap[f"col_{c}_{board[r][c]}"] += 1
                checkMap[f"box_{r//3}_{c//3}_{board[r][c]}"] +=1
                if (checkMap[f"row_{r}_{board[r][c]}"] > 1 or 
                    checkMap[f"col_{c}_{board[r][c]}"] > 1 or 
                    checkMap[f"box_{r//3}_{c//3}_{board[r][c]}"] > 1):
                    return False
        
        return True
                
        
