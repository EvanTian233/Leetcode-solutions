### Summary
Third day for array - little bit stuck on 2d-array.

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
