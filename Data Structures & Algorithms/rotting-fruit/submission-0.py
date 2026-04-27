class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        rows, cols= len(grid), len(grid[0])
        fresh_count = 0
        t = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        while q and fresh_count > 0:
            t += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh_count -= 1
                            q.append((nr, nc))
        return t if fresh_count == 0 else -1