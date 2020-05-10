Insertion into a Trie takes O(n) time because the functon iterates over every input char n. Finding a Trie node that represents a prefix is the same. These operations are not affected by the size of the Trie because a dictionary is used for operations in O(1).

Time complexity for finding all suffixes depends on the size of the Trie. If an average node has k = 5 children, and the average depth of one suffix is n = 3 (three nodes deep), the recursive function is executed 5 + 5 * 5 + 5 * 5 * 5, so the time complexity is O(k^n).

Space complexity is O(n) for a total n characters of nodes (children).
