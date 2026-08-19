class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addPos(r, c):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or
                grid[r][c] == -1):
                return

            # If cell value is INF (As 0 already added first to queue and visited)
            visited.add((r, c))
            q.append([r, c])

        # First add the visits and q with the Treasure chest (r, c)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append([r, c])

        d = 0 # distance from nearest treasure chest
        while q: # Until queue is empty
            for i in range(len(q)): # Iterate through each [r, c] in queue
                r, c = q.popleft()
                grid[r][c] = d # Change the value to distance from nearest tc
                # Go through each neighbouring cell
                addPos(r + 1, c)
                addPos(r - 1, c)
                addPos(r, c + 1)
                addPos(r, c - 1)
            d += 1 # Iterate distance when it goes through a single layer of cells (Same distance cells from treasure chest)
        


        
