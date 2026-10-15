class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        
        def dfs(r, c, charInt):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] != word[charInt]:
                return            
            visit.add((r, c))
            if charInt == len(word) - 1:
                return True

            visit.add((r, c))
            res = (dfs(r + 1, c, charInt + 1) or
                   dfs(r - 1, c, charInt + 1) or
                   dfs(r, c + 1, charInt + 1) or
                   dfs(r, c - 1, charInt + 1))
            visit.remove((r, c))  # backtrack
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False