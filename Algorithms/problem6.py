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

def test(tests):
    for item in tests:
        minmax = find_minmax(item)
        print("max: {} min: {}".format(minmax.max, minmax.min))


test(tests)