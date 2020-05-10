def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if len(input_list) == 0:
        return -1

    return search(input_list, 0, len(input_list) - 1, number)




def search(arr, left_index, right_index, target):

    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_element = arr[mid_index]

    if mid_element == target:
        return mid_index

    if arr[left_index] <= mid_element:

        # Leftmost item is smaller than middle element,
        # pivot cannot be in left part, so it is sorted        
        # (equality: there is no left part)

        if arr[left_index] <= target and target < mid_element:
            
            # Target is located in the left part 
            return search(arr, left_index, mid_index - 1, target)
            
        else:
            
            # Target is located in the right part 
            return search(arr, mid_index + 1, right_index, target)

    elif mid_element <= arr[right_index]:

        # Rightmost item is bigger than middle element,
        # pivot cannot be in right part, so it is sorted
        # (equality: there is no right part)
        
        if mid_element <= target and target < arr[right_index]:

            # Target is located in the right part
            return search(arr, mid_index + 1, right_index, target)

        else:

            # Target is located in the right part
            return search(arr, left_index, mid_index - 1, target)

    return -1


print('\n\n___________ TEST 1 ___________')

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index

    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print(f'Returned: {linear_search(input_list, number)}, Expected: {rotated_array_search(input_list, number)}')

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


print('\n\n___________ TEST 2 ___________')

print(rotated_array_search([], 5))
# Expected: -1

print('\n\n___________ TEST 3 ___________')

print(rotated_array_search([2, 3, 4, 1], 1))
# Expected: 3

