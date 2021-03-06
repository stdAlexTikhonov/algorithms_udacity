class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            self.head.next = self.tail
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def remove_first(self):
        output = self.head
        self.head = self.head.next
        self.size -= 1
        return output

class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
        self.linked_list = LinkedList()

    def get(self, key):
        if key in self.cache:
             return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if self.capacity and self.capacity > 0:
            self.cache[key] = value
            new_node = Node(value, key)
            if self.linked_list.size < self.capacity:
                self.linked_list.add(new_node)
                self.cache[key] = value
            else:
                first_item = self.linked_list.remove_first()
                del self.cache[first_item.key]
                self.linked_list.add(new_node)
                self.cache[key] = value
        else:
            print("Cannot set cache with capacity of {}".format(self.capacity))




#Test1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache


#Test2 0
cache2 = LRU_Cache(0)
cache2.set(1, 1)
print(cache2.get(1))

#Test2 -1
cache2 = LRU_Cache(-1)
cache2.set(1, 1)
print(cache2.get(1))

#Test3 High capacity
capacity = 100
chache3 = LRU_Cache(capacity)
capacity += 10

for i in range(capacity + 1):
    chache3.set(i, i)

print(chache3.get(capacity))




"""
To solve this problem I used LinkedList and built-in dict structure.

LinkedList is good in deleating and inserting we can do it in O(1).

And Dict good in searching. 
In case of huge amount of data and heigh capacity and collisions we can use HashTable.


"""