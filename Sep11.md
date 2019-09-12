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
      <html>
      <head>
      </head>
    </html>
        int binarySearch(int arr[], int x) 
    { 
        int l = 0, r = arr.length - 1; 
        while (l <= r) { 
            int m = l + (r - l) / 2; 
  
            // Check if x is present at mid 
            if (arr[m] == x) 
                return m; 
  
            // If x greater, ignore left half 
            if (arr[m] < x) 
                l = m + 1; 
  
            // If x is smaller, ignore right half 
            else
                r = m - 1; 
        } 
  
        // if we reach here, then element was 
        // not present 
        return -1; 
