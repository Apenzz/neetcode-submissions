class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        numIsland = 0

        def dfs(start_node: Tuple()) -> None:
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            stack = collections.deque()
            stack.append(start_node)

            while stack:
                current_node = stack.pop()
                row, col = current_node
                if current_node not in visited:
                    visited.add(current_node)
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if r in range(rows) and c in range(cols) and grid[r][c] == "1":
                            stack.append((r,c))

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs((r,c))
                    numIsland += 1
        
        
        return numIsland

