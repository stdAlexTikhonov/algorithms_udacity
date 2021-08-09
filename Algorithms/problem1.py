import math

def sqrt(k):
    low = 0
    high = k
    if k > 0:
        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid

            if mid_squared <= k:
                low = mid + 1
            else:
                high = mid - 1
            
        return low - 1
    else:
        print('Input is less or equal to 0')
        return -1

def test_function(test_case, ans):

    if sqrt(test_case) == ans:
        print("Pass")
    else:
        print(sqrt(test_case))
        print("Fail")

test_function(300, 17)
test_function(-1, -1)
test_function(0, -1)
