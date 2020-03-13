/*

242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

*/

class Solution {
    public boolean isAnagram(String s, String t) {
        // Sorting
        if (s.length() != t.length()) {
            return false;
        }
        char[] str1 = s.toCharArray();
        char[] str2 = t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        return Arrays.equals(str1, str2);
    }
    
    public boolean isAnagram2(String s, String t) {
        // Hash table
        if(s.length() != t.length()){
            return false;
        }
        int[] counter = new int[26];
        for(int i=0; i < s.length();i++){
            counter[s.charAt(i) - 'a']++;
            counter[t.charAt(i) - 'a']--;
        }
        for(int count : counter){
            if(count != 0){
                return false;
            }
        }
        return true;
    }    
}