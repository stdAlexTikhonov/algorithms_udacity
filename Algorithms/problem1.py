def sqrt(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
        
    return low - 1

# in naive approach To find squared number of k we have to go from 0 all the way to k, and check result of number ^ 2
# with binary search we can do it faster