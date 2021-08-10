class Heap:
    def __init__(self, size):
        self.cbt = [None for i in range(size)]
        self.next_index = 0


    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break



    def insert(self, data):
        self.cbt[self.next_index] = data

        self._up_heapify()
        
        self.next_index += 1

        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for i in range(len(self.cbt) * 2)]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def size(self):
        return self.next_index

    def remove(self):
        if self.size() == 0:
            return None

        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        self.cbt[0] = last_element
        self.cbt[self.next_index] = to_remove

        self._down_heapify()

        return to_remove

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            #check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            #check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            if left_child is not None:
                min_element = min(parent, left_child)

            if right_child is not None:
                min_element = min(right_child, min_element)

            #check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent = right_child_index


heap = Heap(10)

heap.insert(5)
heap.insert(4)
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.remove()
heap.remove()
heap.remove()

print(heap.cbt)