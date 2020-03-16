/*

326. Power of Three

https://leetcode.com/problems/power-of-three/

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false

*/

class IsPowerOfThree {
    public boolean isPowerOfThree(int n) {
        return (n>0) && (n==1 || (n%3 == 0 && isPowerOfThree(n/3)));
    }
}


