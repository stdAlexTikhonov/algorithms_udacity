def bubble_sort(l):
    indexing_length = len(l) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if l[i] > l[i+1]:
                sorted = False
                l[i], l[i+1] = l[i+1], l[i]
    
    return l