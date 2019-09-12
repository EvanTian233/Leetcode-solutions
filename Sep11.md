### Summary
Second day for array - already found a pattern.

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
