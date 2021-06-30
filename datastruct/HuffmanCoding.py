import sys
from collections import Counter
from heapq import heappush, heappop, heapify

class Node:
    def __init__(self, freq = None, value = '', left = None, right = None):
        self.freq = freq
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

class Tree:
    def __init__(self, root = None):
        self.root = root

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, "")
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, "")
        elif traversal_type == "post":
            return self.post_order(self.root, "")
        elif traversal_type == "level":
            return self.levelorder_print(self.root)
        else:
            print("Traversal type " + traversal_type + " is not supported")

    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.freq) + ".")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        
    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert(node, self.root)

    def _insert(self, node, cur_node):
        if node.freq > cur_node.freq:
            save = cur_node.freq
            cur_node.freq = node.freq
            node.freq = save

        if node.freq <= cur_node.freq:
            if cur_node.left is None:
                cur_node.left = node
            else:
                self._insert(node, cur_node.left)
        elif node.freq > cur_node.freq:
            if cur_node.right is None:
                cur_node.right = node
            else:
                self._insert(node, cur_node.right)



def transform(x):
    return Node(x[1], x[0])







def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":

    codes = {}

    def getBinaryCode(node, code):
        if not node.left and not node.right:
            node.code = code
            codes[node.value] = code
            return
        getBinaryCode(node.left, code + '0')
        getBinaryCode(node.right, code + '1')

    def huffman_encoding(data):
        frequency = Counter(data)
        as_list = list(frequency.items())
        heap = list(map(transform, as_list))
        heapify(heap)

        while len(heap) > 1:
            f1 = heappop(heap)
            f2 = heappop(heap)
            new_node = Node(f1.freq + f2.freq, f1.value + f2.value, f1, f2)
            heappush(heap, new_node)

        last_node = heappop(heap)
        getBinaryCode(last_node, '')

        output = ''

        for letter in data:
            output += str(codes[letter])

        return output


    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    
    encoded_data = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))