def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if len(input_list) == 0:
        print('Array is empty')
        return -1

    left = 0
    right = len(input_list) - 1

    while (left < right):
        mid = (left + right) // 2
        if input_list[mid] > input_list[right]:
            left = mid + 1
        else:
            right = mid

    start = left
    left = 0
    right = len(input_list) - 1

    if number >= input_list[start] and number <= input_list[right]:
        left = start
    else:
        right = start

    while (left <= right):
        mid = (left + right) // 2

        if number == input_list[mid]:
            return mid
        elif number > input_list[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])

# The idea is to find the pivot point, divide the array in two sub-arrays and perform binary search.
# The main idea for finding pivot is – for a sorted (in increasing order) and pivoted array, pivot element is the only element for which next element to it is smaller than it.
# Using the above statement and binary search pivot can be found.
# After the pivot is found out divide the array in two sub-arrays.
# Now the individual sub – arrays are sorted so the element can be searched using Binary Search.