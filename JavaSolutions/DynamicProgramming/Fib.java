/*

509. Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

*/

class Fib {
    public int fib(int N, int[] memo) {
        if (N == 0){
            return 0;
        }
        if (N == 1) {
            return 1;
        }
        memo[0] = 0;
        memo[1] = 1;
        
        if (memo[N] < 1){
            memo[N] = fib(N-1, memo) + fib(N-2,memo);
        }
        
        return memo[N];
    }
    
    public int fib(int N) {
        int[] memo = new int[N+1];
                           

        
        return fib(N, memo);
    }
}