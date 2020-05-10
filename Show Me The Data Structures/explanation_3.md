Steps to encoding are:

1. Get frequencies: A dictionary is used for constant time access to each data char (key). As every char is accessed, time complexity is O(k) for k chars (not considered because it is reading input data), and space complexity (n) for n distinct chars, or (k) for k chars.

2. Build list of tuples: List is needed because nodes (with chars values) will be sorted. Iteration takes O(n) time for n distinct chars.

3. Build tree: Subtrees are created and their roots with the frequency sums of nodes are inserted to the list. Two nodes linked to a root node, the root node is linked to another node etc. In total this operation is executed n-1 times and in each execution, the sorted list is traversed, so time complexity is O(n^2)

4. Determine codes: The tree is traversed recursively to append a binary digit for every node visit. Time complexity is O(v) for all the v nodes visited. Worst case, all chars have the same length code, so they are at the bottom of the tree, so nodes are n + n/2 + ... + 2 + 1. Time complexity then is O(n) for n distinct chars. Tree also has space complexity (n) for the same reason.

5. Encode: Having a dictionary of the codes for constant time access, the output can be constructed. Time is O(k) for k input data length, same as output string, space is (k) also.

Decoding:

The tree is traversed. For encoded character k, its binaries are used to access the respective node. Because the tree, in the worst case, has a depth depending on n distinct chars, this operation is executed a number of times depending on k and lasts a time depending on n. So time complexity is O(k*n). Space complexity is O(k).

Overall, worst case time complexity is O(n^2) where n is the number of distinct characters, for the placement of roots inside the sorted list, and space complexity is (n), for n distinct chars in the tree.
