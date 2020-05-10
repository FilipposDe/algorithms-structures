def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    
    max_i = 0
    max_num = ints[max_i]
    min_i = 0
    min_num = ints[min_i]

    for i, num in enumerate(ints):
        if num > max_num:
            max_num = num
            max_i = i
        if num < min_num:
            min_num = num
            min_i = i

    return (min_num, max_num)




print('\n\n___________ TEST 1 ___________')

print(get_min_max([1]))
# Expected: 1, 1


print('\n\n___________ TEST 2 ___________')

print(get_min_max([1, 2, 3]))
# Expected: 1, 3


print('\n\n___________ TEST 3 ___________')

print(get_min_max([999, -999]))
# Expected: -999, 999

print('\n\n___________ TEST 4 ___________')

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
