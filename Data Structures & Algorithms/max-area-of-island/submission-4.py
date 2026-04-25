import collections
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def bfs(r, c):
            nonlocal maxArea
            queue = collections.deque()
            queue.append((r,c))
            grid[r][c] = 0
            area = 0

            while queue:
                row, col = queue.popleft()
                area += 1
                for dr, dc in directions:
                    if row + dr in range(rows) and col + dc in range(cols) and grid[row+dr][col+dc] == 1:
                        grid[row+dr][col+dc] = 0
                        queue.append((row + dr, col + dc))
            
            maxArea = max(area, maxArea)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)
        return maxArea