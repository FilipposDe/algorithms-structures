class DoubleLinkedNode:

    def __init__(self, key, value):
        # Store key for backwards reference on deletion
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def move_existing_node_to_head(self, node):
        if self.head is node:
            return
        # Store prev left and right nodes, prev head
        prev_head = self.head
        prev_right = node.right
        prev_left = node.left
        # Put node at head
        self.head = node
        # Update node to point to prev head
        node.right = prev_head
        # Update prev left node to point to prev right
        prev_left.right = prev_right
        # Set prev left node as tail if node was tail
        if self.tail is node:
            self.tail = prev_left
        # Update prev right node if it existed to point to prev left
        if prev_right is not None:
            prev_right.left = prev_left

    def append_node_left(self, node):
        # If linked list is empty
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return
        # Store prev head
        prev_head = self.head
        # Set new node as head
        self.head = node
        # Update prev head to point to node
        prev_head.left = node
        # Update node to point to prev head
        node.right = prev_head

        self.size += 1

    def pop_right(self):
        # Nothing to delete if List is empty
        if self.tail is None:
            return None
        # Store prev tail
        prev_tail = self.tail
        # If List has one node
        if self.tail is self.head:
            self.tail = None
            self.head = None
            self.size -= 1
            return prev_tail        

        # Update tail to be prev tail left
        self.tail = prev_tail.left
        # Link new tail left to None
        prev_tail.left.right = None

        self.size -= 1
        return prev_tail

    def __repr__(self):
        result = '< '
        curr_node = self.head
        while curr_node is not None:
            result += " " + str(curr_node.value) + " "
            curr_node = curr_node.right
        result += ' >'
        return result


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        # item_nodes is a dict where keys are cache keys, 
        # values are corresponding nodes,
        # values of the nodes are cache values
        self.item_nodes = dict()
        # Use DoubleLinkedList to keep track of last used key
        self.items_linked_list = DoubleLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.item_nodes.get(key) is None:
            return -1

        node = self.item_nodes[key]
        self.items_linked_list.move_existing_node_to_head(node)

        # print(f"=== Get key: {key} ===")
        # for e in (self.item_nodes):
        #     print(f'key = {str(e)}, value = {str(self.item_nodes[e].value)}')
        # print('-------------------')
        # print(f'cache LinkedList >>> {self.items_linked_list}')
        # print("===================", end='\n\n\n')

        return node.value

    def set(self, key, value):

        if key is None:
            return

        # Set the value if the key is not present in the cache. 
        if key in self.item_nodes:
            return

        # If the cache is at capacity remove the oldest item.
        capacity_to_be_exceeded = len(self.item_nodes) >= self.capacity
        if capacity_to_be_exceeded:
            removed_node = self.items_linked_list.pop_right()
            key_to_remove = removed_node.key
            del removed_node
            del self.item_nodes[key_to_remove]

        new_node = DoubleLinkedNode(key, value)
        self.item_nodes[key] = new_node
        self.items_linked_list.append_node_left(new_node)

        # print(f"=== Set key: {key}, value: {value} ===")
        # for e in (self.item_nodes):
        #     print(f'key = {str(e)}, value = {str(self.item_nodes[e].value)}')
        # print('-------------------')
        # print(f'cache LinkedList >>> {self.items_linked_list}')
        # print("===================", end='\n\n\n')






########################################################
##                      TEST CASES                    ##
########################################################

print("\n\n___ TEST 1 ___")
cache = LRU_Cache(5)

cache.set(1, "One")
cache.set(2, "Two")

print(cache.get(3))
# Expected -1

cache.set(3, "Three")
cache.set(4, "Four")

print(cache.get(1))
# Expected 'One'

cache.set(5, "Five")
cache.set(6, "Six")

print(cache.get(2))
# Expected -1


print("\n\n___ TEST 2 ___")
cache = LRU_Cache(5)

cache.set(1, "One")
cache.set(2, None)
cache.set(3, "Three")
cache.set(4, "Four")

print(cache.get(2))
# Expected None


print("\n\n___ TEST 3 ___")
cache = LRU_Cache(5)

cache.set(1, "One")
cache.set(None, "Two")
cache.set(3, "Three")
cache.set(4, "Four")

print(cache.get(None))
# Expected -1


print("\n\n___ TEST 4 ___")
cache = LRU_Cache(10)

for i in range(20):
    cache.set("key" + str(i), "value" + str(i))

print(cache.get('key5'))
# Expected -1

print(cache.get('key19'))
# Expected 'value19'



print("\n\n___ TEST 5 ___")
cache = LRU_Cache(1000)

for i in range(2000):
    cache.set("key" + str(i), "value" + str(i))

print(cache.get('key1500'))
# Expected 'value1500'









# our_cache = LRU_Cache(5)

# our_cache.set(1, 1)
# our_cache.set(2, 2)
# our_cache.set(3, 3)
# our_cache.set(4, 4)


# our_cache.get(1)       # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

# our_cache.set(5, 5)
# our_cache.set(6, 6)

# # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
# our_cache.get(3)
