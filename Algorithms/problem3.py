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

    return quick_sort(items_greater) + [pivot] + quick_sort(items_lower)

def solve(arr):
    n = len(arr)
    # sort the array
    arr = quick_sort(arr)
 
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

#The idea is to use an auxiliary array. 
# We maintain two pointers one to leftmost or smallest element and other to rightmost or largest element. 
# #We move both pointers toward each other and alternatively copy elements at these pointers to an auxiliary array. 
# Finally, we copy the auxiliary array back to the original array.