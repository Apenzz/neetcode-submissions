class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(i, j, index):
            # Base case
            if board[i][j] != word[index]:
                return False
            
            if index == len(word) - 1:
                return True
            
            tmp = board[i][j]
            board[i][j] = "#"
                
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if ni in range(rows) and nj in range(cols):
                    if backtrack(ni, nj, index + 1):
                        return True
                    
            board[i][j] = tmp
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
    

