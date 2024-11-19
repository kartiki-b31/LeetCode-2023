class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, idx, visited):
            if idx >= len(word):
                return True
            
            moves = [(1,0), (0,1), (-1,0), (0,-1)]

            for move in moves:
                new_row = row + move[0]
                new_col = col + move[1]

                if 0<= new_row < len(board) and 0 <= new_col < len(board[0]) and (new_row, new_col) not in visited:

                    visited.add((new_row, new_col))
                    if board[new_row][new_col] == word[idx]:
                        if dfs(new_row, new_col, idx+1, visited):
                            return True
                    visited.remove((new_row, new_col))

            return False
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    if dfs(i,j,1,visited):
                        return True

        return False
