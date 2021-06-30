import hashlib
import time

class Block:

    def __init__(self, data, previous_hash = hashlib.sha256().hexdigest()):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "{}{}{}".format(self.timestamp, self.data, self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.root = None
        self.tail = None
        self.size = 0

    def add(self, node):
        if not self.root:
            self.root = node
            self.tail = self.root
        else:
            self.tail.next = node
            self.tail = self.tail.next


block1 = Block(100)
block2 = Block(200, block1.hash)
block3 = Block(300, block2.hash)
block4 = Block(400, block3.hash)
block5 = Block(500, block4.hash)

blockchain = Blockchain()

blockchain.add(block1)
blockchain.add(block2)
blockchain.add(block3)
blockchain.add(block4)
blockchain.add(block5)






