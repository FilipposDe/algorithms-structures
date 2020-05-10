The function was implemented with a binary search. Instead of searching for a number, it searches for the square root, which means an examined element is raised to the power of two and compared to the number. The root is searched in all non negative integers up to the number.

Because the exact value might fall between two integers, every time a mid_n is selected and the root, for example, is located to the left, it might be the case that it is also to the right of the immediate previous integer. For this reason, if that is the case, the recursive function is called and reaches a base case (smallest of the two integers is returned because of floor specificaton).

Time complexity is that of binary search O(logn) for number n. Space complexity is O(1) as it is the same for any n. 