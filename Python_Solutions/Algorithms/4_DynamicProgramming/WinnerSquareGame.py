"""
1510. Stone Game IV
https://leetcode.com/problems/stone-game-iv/

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        if int(math.sqrt(n)) ** 2 == n:
            return True
        
        dp = [None] * (n+1)
        dp[0] = False
        steps = sorted([ele ** 2 for ele in range(1, int(math.sqrt(n)) + 1)], reverse=True)
        
        for i in range(n):
            for step in steps:
                if i + step <= n:
                    if dp[i + step]:
                        continue
                    else:
                        dp[i + step] = (False if dp[i] else True)
        
            if dp[-1]:
                return True
        return False
                            
        

