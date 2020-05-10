Router operations:

split_path: Time complexity is O(n) because splitting the path needs iterating over n characters. Space complexity is O(k) for k items of the created list.


add_handler: Time complexity is O(n) for n characters(split_path). After that, insert on the Trie has time complexity O(k) for k items in the list of path parts because every item is checked on a dictionary (insert function of Node takes linear time). Space complexity is similarly O(k) because of the split list. Overall, assuming every path part has the same average number of characters, time and space complexity is O(n) for n input characters. 

lookup: Similarly, split_path has time complexity O(n) for n chars, find function of Trie has time and space complexity O(k) for k path parts (list items). Overall, time and space complexity is O(n) for n input characters.