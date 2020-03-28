
/*

91. Decode Ways

https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

*/

public class NumDecodings {
    public int numDecodings(String s) {
        if (s.isEmpty() || s.charAt(0) - '0' == 0) return 0;
        int[] memo = new int[s.length()+1];
        memo[0] = 1;
        memo[1] = 1;
        
        for(int i=1; i<s.length();i++){
            int curr = s.charAt(i) - '0';
            int prev = s.charAt(i-1) - '0';
            
            // can't make progress, return 0
            if (prev == 0 && curr == 0 || (curr == 0 && (prev * 10 + curr > 26))){
                return 0;
            }
            
            else if(prev == 0 || (prev*10 + curr)>26){
                memo[i+1] = memo[i];
            }
            
            else if (curr == 0){
                memo[i+1] = memo[i-1];
            }
            else{
                memo[i+1] = memo[i-1]+memo[i];
            }
        }  
        return memo[memo.length-1];                


    }    
    public int numDecodings2(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }
        int n = s.length();
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for(int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i-1, i));
            int second = Integer.valueOf(s.substring(i-2, i));
            if(first >= 1 && first <= 9) {
               dp[i] += dp[i-1];  
            }
            if(second >= 10 && second <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}