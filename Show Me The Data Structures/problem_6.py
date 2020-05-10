class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def lists_item_occurences(lists):
    # Returns a dictionary, with all the items as keys. Each value is a
    # dictionary, including the lists where the item is contained as keys,
    # and True as values

    item_occurences = dict()

    for llist in lists:

        if type(llist) is not LinkedList:
            return item_occurences
        node = llist.head

        while node is not None:
            lists_where_value_ocurred = item_occurences.get(node.value, dict())   
            lists_where_value_ocurred[llist] = True

            item_occurences[node.value] = lists_where_value_ocurred

            node = node.next

    return item_occurences

def union(llist_1, llist_2):

    all_items = lists_item_occurences([llist_1, llist_2])
    union = LinkedList()

    for item in all_items:
        union.append(item)

    return union

    
def intersection(llist_1, llist_2):
    
    all_items = lists_item_occurences([llist_1, llist_2])
    intersection = LinkedList()

    for item in all_items:
        lists_dict = all_items[item]
        if len(lists_dict) == 2:
            # If both lists are in the item value (an inner dictionary)
            intersection.append(item)

    return intersection



########################################################
##                      TEST CASES                    ##
########################################################

print("\n\n___ TEST 1 ___")

element_1 = [1, 2, 3, 5, 6, 7, 999]
element_2 = [1, 2, 3, 5, 6, 7, 998]
ll1 = LinkedList()
ll2 = LinkedList()

for i in element_1:
    ll1.append(i)

for i in element_2:
    ll2.append(i)

print(union(ll1, ll2))
# Expected 1, 2, 3, 5, 6, 7, 999, 998
print(intersection(ll1, ll2))
# Expected 1, 2, 3, 5, 6, 7


print("\n\n___ TEST 2 ___")

element_1 = [1, 2, 3]
element_2 = [4, 5, 6]
ll1 = LinkedList()
ll2 = LinkedList()

for i in element_1:
    ll1.append(i)

for i in element_2:
    ll2.append(i)

print(union(ll1, ll2))
# Expected 1, 2, 3, 4, 5, 6
print(intersection(ll1, ll2))
# Expected []



print("\n\n___ TEST 3 ___")

element_1 = []
ll1 = LinkedList()

for i in element_1:
    ll1.append(i)

print(union(ll1, None))
# Expected []
print(intersection(ll1, None))
# Expected []


# # Test case 1

# linked_list_1 = LinkedList()
# linked_list_2 = LinkedList()

# element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
# element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

# for i in element_1:
#     linked_list_1.append(i)

# for i in element_2:
#     linked_list_2.append(i)

# print(union(linked_list_1, linked_list_2))
# print(intersection(linked_list_1, linked_list_2))

# # Test case 2

# linked_list_3 = LinkedList()
# linked_list_4 = LinkedList()

# element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
# element_2 = [1, 7, 8, 9, 11, 21, 1]

# for i in element_1:
#     linked_list_3.append(i)

# for i in element_2:
#     linked_list_4.append(i)

# print(union(linked_list_3, linked_list_4))
# print(intersection(linked_list_3, linked_list_4))
