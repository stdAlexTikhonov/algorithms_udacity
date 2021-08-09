# The idea is to use an auxiliary array.

# We maintain two pointers one to leftmost or smallest element and other to rightmost or largest element.

# #We move both pointers toward each other and alternatively copy elements at these pointers to an auxiliary array.

# Finally, we copy the auxiliary array back to the original array.

Time complexity: O(n\*log(n))
Space complexity: O(n\*log(n)) - avarage space complexity of quick sort
