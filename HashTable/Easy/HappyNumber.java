/*

202. Happy Number

https://leetcode.com/problems/happy-number/

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

*/


class HappyNumber {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while (n != 1){
            int current = n;
            int sum = 0;
            while (current != 0){
                sum += (current % 10) * (current % 10) ;
                current /= 10;
            }
            if(seen.contains(sum)){
                return false;
            }
            seen.add(sum);
            n = sum;
        }
        return true;
    }
}