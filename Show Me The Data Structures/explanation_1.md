The LRU cache is using a dictionary and a double linked list. The dictionary holds the keys of the cache with the respective nodes (which are containing values). 

The double linked list contains the nodes, with each node representing a distinct key, ordered by last use. 

The dictionary was used because setting and getting values has time complexity O(1). Appending and popping functions from the list also have O(1), so does moving a node to the head, because the node is first retrieved by the dictionary instead of being searched linearly.

Overall, all functions have a time complexity of O(1). Space complexity is (1), for a given capacity, or O(n*2) = O(n) for n units of capacity. 