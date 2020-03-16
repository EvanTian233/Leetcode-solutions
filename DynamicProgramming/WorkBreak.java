/*

139. Word Break

https://leetcode.com/problems/word-break/

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

*/

class WordBreak {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] memo = new boolean[s.length() + 1];
        memo[0] = true;
        
        for(int i = 1; i<=s.length(); i++){
            for (int j = 0; j<s.length(); j++){
                if(memo[j] && wordDict.contains(s.substring(j, i))){
                    memo[i] = true;
                    break;
                }
            }
        }
        return memo[s.length()];
    }
}




