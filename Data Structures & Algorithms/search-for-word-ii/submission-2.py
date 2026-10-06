class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(i, j, node, word):
            if i < 0 or j < 0 or i == ROWS or j == COLS or (i, j) in visit or board[i][j] not in node.children:
                return

            visit.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.endOfWord:
                res.add(word)

            dfs(i + 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j - 1, node, word)
            visit.remove((i, j))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, root, "")
        
        return list(res)
        