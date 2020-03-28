/*

28. Implement strStr()

https://leetcode.com/problems/implement-strstr/

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

*/


class StrStr {
    public int strStr(String haystack, String needle) {
        if (needle.isEmpty()) return 0;
        for(int i = 0; i <= haystack.length() - needle.length(); i++){
            for (int j=0; j<needle.length() & haystack.charAt(i+j) == needle.charAt(j); j++){
                if (j == needle.length() - 1) return i;
            }
        }
        return -1;
    }
}


