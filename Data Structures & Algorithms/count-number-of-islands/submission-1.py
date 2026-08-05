class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visits, islands = set(), 0

        def dfs(r, c):

            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visits or
                grid[r][c] == "0"):
                
                return
            
            visits.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r , c + 1)
            dfs(r , c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visits:
                    dfs(r, c)
                    islands += 1
        
        return islands

        