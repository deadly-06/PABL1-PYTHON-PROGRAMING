class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            # If we've matched all letters
            if index == len(word):
                return True
            
            # Check bounds and current cell
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 directions
            found = (dfs(r+1, c, index+1) or
                     dfs(r-1, c, index+1) or
                     dfs(r, c+1, index+1) or
                     dfs(r, c-1, index+1))
            
            # Restore cell (backtrack)
            board[r][c] = temp
            
            return found
        
        # Try starting DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
