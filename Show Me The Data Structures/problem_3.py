import sys

####################
#  Helper classes  #
####################

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Comparison functions for nodes that have a frequency
    # tuple as value

    def __lt__(self, other):
        if type(self.value) is tuple:
            return self.value[0] < other.value[0]
        return self < other

    def __gt__(self, other):
        if type(self.value) is tuple:
            return self.value[0] > other.value[0]
        return self > other

    def __eq__(self, other):
        if type(self.value) is tuple:
            return self.value[0] == other.value[0]
        return self == other

    def __ge__(self, other):
        if type(self.value) is tuple:
            return self.value[0] == other.value[0] or self.value[0] > other.value[0]
        return self >= other

    def __repr__(self):
        return 'NODE >> value: ' + str(self.value) + ' '


class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        curr_node = self.root

        while True:
            if value == curr_node.value:
                # If value exists, do nothing
                return
            elif value > curr_node.value:
                if curr_node.right is not None:
                    curr_node = curr_node.right
                    continue
                else:
                    curr_node.right = Node(value)
                    return
            elif value < curr_node.value:
                if curr_node.left is not None:
                    curr_node = curr_node.left
                    continue
                else:
                    curr_node.left = Node(value)
                    return

    def to_list(self):
        values = []

        def traverse(node):
            if node is None:
                return
            values.append(node.value)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return values
            

####################
# Helper functions #
####################

def get_char_frequencies_dict(string):
    # Example return value: { 'a': 2, 'e': 9, 'i': 1 }
    freq_dict = dict()

    for char in string:
        curr_freq = freq_dict.get(char, 0)
        freq_dict[char] = curr_freq + 1
    
    return freq_dict


def dict_to_tuples_nodes_list(dictionary):
    # Example return value: [ ( 2, 'a' ), ( 9, 'e' ), ( 1, 'i' ) ]
    nodes_list = list()

    for key in dictionary:
        reverse_tuple = (dictionary[key], key)
        node = Node(reverse_tuple)
        nodes_list.append(node)

    return nodes_list


def get_linking_sum_root(tuple_node_1, tuple_node_2):
    # Example return value:
    #            ( 3, '' ) <- Returned root
    #           /           \
    #   ( 2 , 'a')          ( 1, 'i' )
    
    root_value = (tuple_node_1.value[0] + tuple_node_2.value[0], '')
    root = Node(root_value)
    root.left = tuple_node_1
    root.right = tuple_node_2

    return root


def insert_node_to_sorted_list(node, sorted_list):
    # Determines where to insert node so order is kept, and inserts
    insert_index = 0
    for i in range(len(sorted_list) - 1, -1, -1):
        if sorted_list[i] >= node:
            insert_index = i + 1
            break

    sorted_list.insert(insert_index, node)
    


def trim_node(node):
    # Trims frequency from node value (tuple), keeps only string
    old_value = node.value
    node.value = old_value[1]


def build_char_codes_with_trim(node):
    # Recursively access tree nodes, building a list with binary codes and chars.
    # Example return value: [ 0e, 10a, 11i ]
    
    node_char = node.value[1]
    
    # Nodes with a char are leaves because of the Huffman tree build process
    is_leaf = node_char != ''
    if is_leaf:
        trim_node(node)
        return [node_char]

    char_codes = list()

    left_codes = build_char_codes_with_trim(node.left)
    for code in left_codes:
        char_codes.append('0' + code)

    right_codes = build_char_codes_with_trim(node.right)
    for code in right_codes:
        char_codes.append('1' + code)

    trim_node(node)
    return char_codes


def char_codes_list_to_dict(codes_list):
    # Example list item format: '11i'
    # Example return value: [ 'e': 0, 'a': 10, 'i': 11 ]
    result = dict()
    for item in codes_list:
        code = item[:-1]
        char = item[-1]
        result[char] = code

    return result


def fix_tree_with_leaf_root(tree):
    # Example tree arg:
    #            ( 9, 'e' ) 
    #
    # Example return value:
    #            ( 0, '' ) 
    #           /           \
    #   ( 9 , 'e')          ( 9, 'e' )
    
    # Copy to avoid resulting root pointing to same node
    # left and right
    char_node_copy_1 = Node(tree.root.value)
    char_node_copy_2 = Node(tree.root.value)
    
    # Node frequency value (0) does not matter
    new_root = Node((0, ''))
    
    new_root.left = char_node_copy_1
    new_root.right = char_node_copy_2

    tree.root = new_root
    return new_root





####################
#  Main functions  #
####################

def huffman_encoding(data):

    if len(data) == 0:
        return '', None

    frequencies = get_char_frequencies_dict(data)
    freq_tuples_nodes = dict_to_tuples_nodes_list(frequencies)

    freq_tuples_nodes.sort(reverse=True)
    
    while len(freq_tuples_nodes) > 1:
        smallest = freq_tuples_nodes.pop()
        next_smallest = freq_tuples_nodes.pop()

        # Link two smallest by frequency nodes (list is sorted).
        # The linking node (root) is inserted while keeping order 
        root = get_linking_sum_root(smallest, next_smallest)
        insert_node_to_sorted_list(root, freq_tuples_nodes)

    # Tree root is the only remaining node in the list
    tree = Tree(freq_tuples_nodes[0])

    # If only one char is used in data, its node was set as tree root.
    # Change tree structure to comply with general structure
    tree_has_single_char = tree.root.value[1] != ''
    if tree_has_single_char:
        tree.root = fix_tree_with_leaf_root(tree)

    char_codes_list = build_char_codes_with_trim(tree.root)
    char_codes_dict = char_codes_list_to_dict(char_codes_list)

    encoded_sequence = ''
    for c in data:
        encoded_sequence += char_codes_dict[c]

    return encoded_sequence, tree




def huffman_decoding(data, tree):

    if len(data) == 0:
        return ''

    decoded = ''

    curr_node = tree.root
    i = 0
    
    while True:

        # If node is leaf (value is char), add char to decoded data
        # and start over from the tree root. Counter i remains the same
        # because it was increased in the previous repetition
        # (note: root cannot be a leaf).
        is_leaf = curr_node.value != ''
        if is_leaf:
            decoded += curr_node.value
            curr_node = tree.root
            continue

        if i >= len(data):
            break

        # Move to next node (left or right)
        curr_binary = data[i]
        if curr_binary == '0':
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

        i += 1

    return decoded







####################
#   Test - size    #
####################

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


########################################################
##                      TEST CASES                    ##
########################################################

## Note: Working directory is 'testdir'

print("\n\n___ TEST 1 ___")

encoded, tree = huffman_encoding('Testing Huffman Coding')
decoded = huffman_decoding(encoded, tree)
print(decoded)
# Expected 'Testing Huffman Coding'

print("\n\n___ TEST 2 ___")

encoded, tree = huffman_encoding('')
decoded = huffman_decoding(encoded, tree)
print(decoded)
# Expected ''

print("\n\n___ TEST 3 ___")

encoded, tree = huffman_encoding('E')
decoded = huffman_decoding(encoded, tree)
print(decoded)
# Expected 'E'