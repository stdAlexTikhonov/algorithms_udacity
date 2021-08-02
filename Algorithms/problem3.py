def solve(arr):
    n = len(arr)
    # sort the array
    arr.sort(reverse=True)
 
    # let two numbers be a and b
    a = 0; b = 0
    for i in range(n):
     
        # Fill a and b with every alternate
        # digit of input array
        if (i % 2 != 0):
            a = a * 10 + arr[i]
        else:
            b = b * 10 + arr[i]
 
    # return the sum
    return [a,b]

resolve = solve([6, 8, 4, 5, 2, 3])
print(resolve)