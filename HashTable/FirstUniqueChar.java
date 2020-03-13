/*

387. First Unique Character in a String

https://leetcode.com/problems/first-unique-character-in-a-string/

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

*/


class FirstUniqChar {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int n = s.length();
        
        for (int i = 0; i< n; i++){
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
            
            }
        for (int i = 0 ; i < n; i++){
            if (map.get(s.charAt(i)) == 1) 
                return i;            
        }
        return -1;
    }
}