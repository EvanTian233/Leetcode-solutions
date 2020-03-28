/*

7. Reverse Integer

https://leetcode.com/problems/reverse-integer/

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

*/



class ReverseInteger {
    public int reverse(int x){
        int result = 0;

        while (x != 0){
            int tail = x % 10;
            int newResult = result * 10 + tail;
            if ((newResult - tail) / 10 != result){ 
                return 0; 
            }
            result = newResult;
            x = x / 10;
        }

        return result;
    }
}

