class Minmax:
    def __init__(self):
        self.min = None
        self.max = None

def find_minmax(arr):
    minmax = Minmax()

    if len(arr) == 0:
        return minmax

    if len(arr) == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax
    
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]


    for i in range(2, len(arr)):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

tests = [
    [],
    [1],
    [37,90],
    [1,90,23,14,23,212,0]
]

def test(tests, fn):
    for item in tests:
        minmax = fn(item)
        if type(minmax) is tuple:
             print("max: {} min: {}".format(minmax[1], minmax[0]))
        else:
             print("max: {} min: {}".format(minmax.max, minmax.min))
       


test(tests, find_minmax)


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

def quick_minmax(arr):
    if len(arr) == 0:
        return (None, None)

    if len(arr) == 1:
        return (arr[0], arr[0])

    sorted_arr = quick_sort(arr)
    length = len(sorted_arr)

    return (sorted_arr[0], sorted_arr[length-1] )

test(tests, quick_minmax)

    