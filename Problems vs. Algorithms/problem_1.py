import math as m


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Only non negative ints
    if type(number) is not int or number < 0:
        return None

    return binary_find_root( 0, number // 2 + 1, number)


def binary_find_root(left_n, right_n, target):

    mid_n = (left_n + right_n) // 2
    mid_n_squared = mid_n * mid_n

    if mid_n_squared == target:
        return mid_n

    two_possible_roots = right_n - left_n == 1
    if two_possible_roots:

        # Determine which number is floored square root

        # Cases where number root is one of the two numbers
        if left_n * left_n == target:
            return left_n
        if right_n * right_n == target:
            return right_n

        # Case where square root falls between the two numbers
        return left_n

    if mid_n_squared > target:

        # Case where real root falls to the left side of mid_n

        # Check if root is immediately before mid_n,
        # mid_n must be included on next call

        mid_n_prev = mid_n - 1
        mid_n_prev_squared = mid_n_prev * mid_n_prev

        if mid_n_prev_squared < target:
            return binary_find_root(mid_n_prev, mid_n, target)

        # mid_n excluded
        return binary_find_root(left_n, mid_n - 1, target)

    if mid_n_squared < target:

        # Case where real root falls to the left side of mid_n

        # Check if root is immediately after mid_n,
        # mid_n must be included on next call

        mid_n_next = mid_n + 1
        mid_n_next_squared = mid_n_next * mid_n_next

        if mid_n_next_squared > target:
            return binary_find_root(mid_n, mid_n_next, target)

        # mid_n excluded
        return binary_find_root(mid_n + 1, right_n, target)



print('\n\n___________ TEST 1 ___________')


for i in range(30):
    correct = m.floor(m.sqrt(i))
    result = sqrt(i)
    print(f'Square root of {i}. Expected {correct}, Received: {result}')
    if correct != result:
        print(
            f'Incorrect square root of {i}. Expected {correct}, Received: {result}')
        break
# Expected: correct == result

print('\n\n___________ TEST 2 ___________')

print(sqrt(-5))
# Expected: None


print('\n\n___________ TEST 3 ___________')

print(sqrt('1'))
# Expected: None
