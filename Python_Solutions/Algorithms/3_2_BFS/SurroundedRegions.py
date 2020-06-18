"""
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R,C = len(board), len(board[0])
        if R<=2 or C<=2:
            return
        queue = collections.deque()
        
        for r in range(R):
            queue.append((r,0))
            queue.append((r, C-1))
            
        for c in range(len(board[0])):
            queue.append((0,c))
            queue.append((R-1, c))
            
        while queue:
            r, c = queue.popleft()
            if 0 <= r < R and 0 <=c < C and board[r][c] == 'O':
                board[r][c] = 'N'
                queue.append((r-1, c))
                queue.append((r+1, c))
                queue.append((r, c+1))
                queue.append((r, c-1))

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'N':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'