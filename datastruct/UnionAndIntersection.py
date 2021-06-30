class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    visited = set()
    curA, curB = llist_1.head, llist_2.head
    while curA:
        visited.add(curA.value)
        curA = curA.next

    while curB:
        visited.add(curB.value)
        curB = curB.next

    result_list = LinkedList()

    for item in visited:
        result_list.append(item)

    return result_list

def intersection(llist_1, llist_2):
    visitedA = set()
    visitedB = set()
    
    curA, curB = llist_1.head, llist_2.head

    while curA:
        visitedA.add(curA.value)
        curA = curA.next

    while curB:
        visitedB.add(curB.value)
        curB = curB.next

    intersec = visitedA.intersection(visitedB)

    result_list = LinkedList()

    for item in intersec:
        result_list.append(item)

    return result_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,3, 4]
element_2 = [4,5,6]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,2,3,4]
element_2 = [3,4,5,6]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
