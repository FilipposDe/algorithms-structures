Binary search was used to find the number. On every execution, left most and right most items are compared to the middle. If, for example, the left is smaller, then it is impossible for the pivot to be within the left part (there would have to be a second pivot to the right so the numbers after the larger middle number would increase and then reset before they circle to the left most item which is small).

This way the correct part can be selected, similar to the binary search.

So time complexity is O(logn) and space is O(logn) for n items in the array, because binary function has depth (number of executions) logn and on every execution O(1) time and space is used.