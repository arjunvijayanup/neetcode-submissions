class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols = set()
        nDiag = set()
        pDiag = set()

        res = []
        board = [["."] * n for i in range(n)] # Create n*n board

        def backtrack(r):
            if r == n: # Reached end (Found combination)
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n): # iterate through each cols
                if c in cols or (r + c) in pDiag or (r - c) in nDiag: # If queens added to existing attack positions
                    continue # Skip iteration

                # incase not present already, add queen attack position to the sets
                cols.add(c)
                pDiag.add(r + c)
                nDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1) # Go to next row

                # Backtrack all existing combinations
                cols.remove(c)
                pDiag.remove(r + c)
                nDiag.remove(r - c) 
                board[r][c] = "." 

        backtrack(0)

        return res

