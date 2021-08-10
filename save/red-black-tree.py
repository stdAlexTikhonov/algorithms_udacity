class Node:
    def __init__(self, value, parent, color):
        self.value = value
        self.parent = parent
        self.color = color
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_value):
        self.insert_helper(self.root, new_value)

    def inser_helper(self, current, new_value):
        if new_value < current.value:
            if current.right:
                self.inser_helper(current.right,current, new_value)
            else:
                current.right = Node(new_value, current, 'red')
                return current.right
        else:
            if current.left:
                self.inser_helper(current.left, current, new_value)
            else:
                current.left = Node(new_value, current, 'red')
                return current.right

    def rebalance(node):
        if node.parent == Node:
            return

        if node.parent.color == 'black':
            return

        if pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            self.rebalance(grandparent(node))