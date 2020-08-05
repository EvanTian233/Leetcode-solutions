"""
211. Add and Search Word - Data structure design
https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

"""


class WordNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        

    def addWord(self, word: str) -> None:

        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                node.children[w] = WordNode()
                node = node.children[w]
                
        node.isEnd = True
        

    def search(self, word: str) -> bool:

        stack = [(self.root, word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isEnd:
                    return True
            elif w[0] == '.':
                for n in node.children.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n,w[1:]))
        return False
            
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)