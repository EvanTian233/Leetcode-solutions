# data_structure_notes
LeetCode started since 2019-09-10

## Array

## Hash Table

## Linked List

## String

## Tree

class Solution {
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        queue.add(root);
        
        while(!queue.isEmpty()){
            TreeNode t1 = queue.poll();
            TreeNode t2 = queue.poll();
            if (t1 == null && t2 == null) continue;
            if (t1 == null || t2 == null) return false;
            if(t1.val != t2.val) return false;
            queue.add(t1.left);
            queue.add(t2.right);
            queue.add(t1.right);
            queue.add(t2.left);            
        }
        return true;
    }
        
}


## Recursion and Dynamic Programming

## Sorting and Searching

* Hash map:
  <br /> Its time complexity is O(1) to find complement since HashMap calculates, not searching, the index based on the key.
    <br /> // Initilization
    <br /> HashMap<Integer, Integer> map = new HashMap<>(); 
    <br /> // map.put(key, value);
    <br /> map.put(target - nums[i], i);
    <br /> // value = map.get(key);   	
    <br /> ans[0] = map.get(nums[i+1]); 		      

* Array questions:
  <br /> Try to use two pointers from the beginning and the back like lo and hi.

## 2019-09-11

### Questions
* #26 Remove Duplicates from Sorted Array
* #33 Search in Rotated Sorted Array
* #34 Find First and Last Position of Element in Sorted Array

### Learned

* If space complexity is O(1)
  <br /> Try to swap the desire output to the front of the array and return from there.

* Binary search
  <br /> Useful with sorted array. 
  <br /> Cooperate with two pointers.
    <html>
      <head>
      </head>
    </html>
    
      int binarySearch(int nums[], int x) 
      { 
        int lo = 0, hi = nums.length - 1; 
        while (lo <= hi) { 
            int mid =  (hi + lo) / 2; 
            
            // Check if x is present at mid 
            if (nums[mid] == x) 
                return mid; 
  
            // If x greater, ignore left half 
            if (nums[mid] < x) 
                lo = mid + 1; 
  
            // If x is smaller, ignore right half 
            else
                hi = mid - 1; 
          } 
        // if we reach here, then element was 
        // not present 
        return -1; 
        }

## 2019-09-12

### Questions
* #48 Rotate Image
* #53 Maximum Subarray  
* #54 Spiral Matrix

### Learned

* 2d-array
  <br /> Track the conners and set different rules when iterating.
  <br /> Two pointers, `i` for each column in a row & `j` for all the rows.
  ```
     for (int j=0; j<matrix.length; j++)
     for (int i=0; i< matrix[j].length; i++)
  ```
* Maximum Subarray
  <br /> If previous subarray is larger than 0, add it to current pointer; otherwise only current pointer.
