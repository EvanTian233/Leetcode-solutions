"""
859. Buddy Strings
https://leetcode.com/problems/buddy-strings/

Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

"""
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or set(A) != set(B): return False       
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:     
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    indices.append(i)       
                if counter > 2:
                    return False       
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]