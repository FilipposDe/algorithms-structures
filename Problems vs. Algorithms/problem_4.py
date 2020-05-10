def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
    # Positions 0's to the start of the array and 2's to the end.
    # All remaining are 1's.

    next_0_index = 0
    next_2_index = len(input_list) - 1

    i = 0
    
    # Traverse the array once.
    # Last index to be checked is next_2_index because it is 
    # one position before the last placed 2.
    while i < next_2_index + 1:

        element = input_list[i]

        if element == 0:

            # Position at next_0_index and put that element in this 0's place
            input_list[i], input_list[next_0_index] = input_list[next_0_index], input_list[i]

            # next_0_index is now taken by a 0, next index is to its right
            next_0_index += 1

            # Increment to check next element. All from i and before are 0's
            i += 1

        if element == 2:
            
            # Position at next_2_index and put that element in this 2's place
            input_list[i], input_list[next_2_index] = input_list[next_2_index], input_list[i]
            
            # next_2_index is now taken by a 2, next index is to its left
            next_2_index -= 1
        
        if element == 1:

            # Leave as is and proceed to next. Might be replaced by a 0 later
            i += 1

    return input_list


print('\n\n___________ TEST 1 ___________')

print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
# Expected: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
# Expected: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
# Expected: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]


print('\n\n___________ TEST 2 ___________')

print(sort_012([1]))
# Expected: [1]


print(sort_012([2]))
# Expected: [2]


print('\n\n___________ TEST 3 ___________')

print(sort_012([]))
# Expected: []


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
