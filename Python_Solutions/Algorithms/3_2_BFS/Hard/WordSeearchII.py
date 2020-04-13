"""
212. Word Search II
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

"""

class Node:
    def __init__(self):
        self.chars = {}
        self.word = False

class Trie:
    def __init__(self):
        self.node = Node()

    def add_word(self, word):
        node = self.node
        for c in word:
            if c not in node.chars:
                node.chars[c] = Node()
            node = node.chars[c]
        node.word = True

class Solution:
    def findWords(self, board, words):
        res = []
        trie = Trie()
        for word in words:
            trie.add_word(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.node, res, "", i, j)
        return res

    def dfs(self, board, trie, res, word, i, j):
        if trie.word:
            res.append(word)
            trie.word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not trie:
            return 
        char = board[i][j]
        if char in trie.chars:
            board[i][j] = '#'
            trie = trie.chars[char]
            for x, y in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                self.dfs(board, trie, res, word + char, i + x, y + j)
            board[i][j] = char