
def mergesort(arr):

    # Descending sort

    if len(arr) <= 1:
        return arr

    mid_index = (len(arr)) // 2

    left_part = arr[:mid_index]
    right_part = arr[mid_index:]
    
    left_part = mergesort(left_part)
    right_part = mergesort(right_part)

    return merge(left_part, right_part)
    

def merge(left_arr, right_arr):
    merged = []

    left_part_index = 0
    right_part_index = 0

    while left_part_index < len(left_arr) and right_part_index < len(right_arr):
        if left_arr[left_part_index] > right_arr[right_part_index]:
            merged.append(left_arr[left_part_index])
            left_part_index += 1
        else:
            merged.append(right_arr[right_part_index])
            right_part_index += 1

    for i in range(left_part_index, len(left_arr)):
        merged.append(left_arr[i])
    for i in range(right_part_index, len(right_arr)):
        merged.append(right_arr[i])

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # Any number is maximized if its digits are sorted by 
    # descending order. This is because if you multiply a digit by 
    # a power of ten, the bigger the digit, the bigger its contribution
    # to the whole number, so the digits positioned left must be the biggest.
    # (9z > z9 for any z < 9, because 9 * 10^1 + z * 10^0 > z * 10^1 + 9 * 10^0  )
    # 
    # So the two numbers will have descending digits.
    # 
    # Also, it order to maximize them, for the same reason, the biggest two digits
    # of the original list must be their first digits, the next biggest must be their second etc.   
    # In other words, we start picking pairs from the end of the original sorted list,
    # and placing each digit in the two numbers. The order (which of the digits goes to which
    # number) does not matter because they both add up to the same amount.

    # List length must be two or bigger 
    if len(input_list) < 2:
        return None

    # Descending order sort list
    input_list_desc = mergesort(input_list)

    # Initialize two numbers
    result_numbers = [input_list_desc[-1], input_list_desc[-2]]

    # Next digit from original list will be put this many places from the left
    next_pos = [1, 1]

    # Index (in result_numbers) of next insertion
    insert_index = 0    

    # Insert from input_list_desc to two numbers, alternating
    # (insert to first, second, first etc. until all numbers from
    # original list have been inserted)
    for i in range(len(input_list_desc) - 3, -1, -1):

        # Multiply digit by this amount to add it to next number
        multiply_by = pow(10, next_pos[insert_index])

        # Increment number by digit * the above amount
        result_numbers[insert_index] += input_list_desc[i] * multiply_by

        # Increment position in this number to insert next        
        next_pos[insert_index] += 1

        # Negate number index for next insertion
        insert_index = not insert_index


    return result_numbers


print('\n\n___________ TEST 1 ___________')

print(sum(rearrange_digits([1, 2, 3, 4, 5])))
# Expected: 573

print(sum(rearrange_digits([4, 6, 2, 5, 9, 8])))
# Expected: 1816


print('\n\n___________ TEST 2 ___________')

print(rearrange_digits([]))
# Expected None


print('\n\n___________ TEST 3 ___________')

print(rearrange_digits([1, 1, 1, 1, 1]))
# Expected [111, 11]
