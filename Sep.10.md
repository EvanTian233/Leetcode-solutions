### Summary
First day in leet code. Starting from array - easy and medium qustions only.

### Questions
* #1 Two Sum
* #11 Container with Most Water
* #15 Three Sum

### Learned

* Hash map:
  <br /> Its time complexity is O(1) to find complement since HashMap calculates, not searching, the index based on the key.
    <br /> // Initilization
    <br /> HashMap<Integer, Integer> map = new HashMap<>(); 
    <br /> // map.put(key, value);
    <br /> map.put(target - nums[i], i);
    <br /> // value = map.get(key);   	
    <br /> ans[0] = map.get(nums[i+1]); 		      

* Array questions:
  <br /> Try use two pointers from the beginning and the bacl like lo and hi.
