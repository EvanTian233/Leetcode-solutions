### Summary
First day in leet code. Starting from array - easy and medium qustions only.

### Questions
* #1 Two Sum
* #11 Container with Most Water
* #15 Three Sum

### Learned
* Hash map:
  Its time complexity is O(1) to find complement since HashMap calculates, not searching, the index based on the key.
        // Initilization
      	HashMap<Integer, Integer> map = new HashMap<>(); 
    		// map.put(key, value);
        map.put(target - nums[i], i);
        // value = map.get(key);
        ans[0] = map.get(nums[i+1]);
* 
