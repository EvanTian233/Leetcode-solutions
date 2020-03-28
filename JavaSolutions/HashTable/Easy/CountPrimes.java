/*

204. Count Primes

https://leetcode.com/problems/count-primes/

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

*/


class CountPrimes {
    public int countPrimes(int n) {
        boolean[] primes = new boolean[n];
        for(int i = 0; i<primes.length; i++){
            primes[i] = true;
        }
        
        for(int i = 2; i*i < primes.length; i++){
            if(primes[i]){
                for (int j = i; j*i < primes.length; j++){
                    primes[j*i]  = false;
                }
            }
        }
        
        int primeCount = 0;
        for (int i = 2; i < primes.length; i++){
            if(primes[i]) primeCount++;
        }
        
        return primeCount;
    }
}