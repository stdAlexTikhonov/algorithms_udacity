# Keep three indices low = 1, mid = 1 and high = N and there are four ranges, 1 to low (the range containing 0), low to mid (the range containing 1), mid to high (the range containing unknown elements) and high to N (the range containing 2).

# Traverse the array from start to end and mid is less than high. (Loop counter is i)

# If the element is 0 then swap the element with the element at index low and update low = low + 1 and mid = mid + 1

# If the element is 1 then update mid = mid + 1

# If the element is 2 then swap the element with the element at index high and update high = high – 1 and update i = i – 1. As the swapped element is not processed

# Print the output array.

Time complexity: O(log(n))

Space complexity: O(1) since we are not using any extra/auxiliary space
