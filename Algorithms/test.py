def lenear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return None


# iterative binary search
def binary_iter_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


def recursive_bin_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return recursive_bin_search(data, target, low, mid - 1)
        else:
            return recursive_bin_search(data, target, mid + 1, high)

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found")


numbers = range(10)

result = lenear_search(numbers, 12)
verify(result)


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

numbers2 = range(10)

result = binary_search(numbers2, 8)

verify(result)


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid + 1:], target)
            else:
                return recursive_binary_search(list[:mid -1], target) 