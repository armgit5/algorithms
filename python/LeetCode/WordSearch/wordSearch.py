# https://leetcode.com/problems/word-search-ii/
# https://www.youtube.com/watch?v=oyRp1IKWqU4
# https://leetcode.com/problems/word-search-ii/discuss/734562/Trie-%2B-DFS-%2B-Backtracking-with-Detailed-Steps
# https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
# https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]


class TrieNode():
    def __init__(self):
        self.children = {}
        word = ""

class Solution(object):
    def __init__(self):
        self.dir = [[0,1], [0,-1], [1,0], [-1,0]]
        self.maxRow = 0
        self.maxCol = 0

    # Build trie from words array
    # ex o->a->t->h
    def buildTrie(self, words):
        root = TrieNode()
        for w in words:
            current = root
            for c in w:
                if c not in current.children:
                    current.children[c] = TrieNode()
                current = current.children[c]
            current.word = w
        return root

    def setMaxRowCol(self, board):
        self.maxRow = len(board)
        self.maxCol = len(board[0])

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return

        # Loop through all char
        for row in range(len(board)):
            for col in range(len(board)):
                # going through all directions

                # try dfs

                for d in self.dir:
                    nextRow = row + d[0]
                    nextCol = col + d[1]


    def isValid(self, row, col):
        if row >= 0 and row < self.maxRow and col >= 0 and col < self.maxCol:
            return True
        else:
            return False

    def dfs(self):
        pass

s = Solution()
root = s.buildTrie(words)
print(root.children['o'].children)
for r in root.children:
    print(r)