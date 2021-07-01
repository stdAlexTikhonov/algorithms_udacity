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

    def add_block(self, data = None):
        if data:
            if not self.root:
                node = Block(data)
                self.root = node
                self.tail = self.root
            else:
                node = Block(data, self.tail.hash)
                if node.timestamp == self.tail.timestamp:
                    print("cannoot insert block with same timestamp")
                    return False
                self.tail.next = node
                self.tail = self.tail.next
            self.size += 1
        else:
            print("Data is Empty")
            return None

    def print(self):
        if self.root:
            curr = self.root
            print("Blockchain: ")
            while curr:
                print(" timestamp: {}, data: {}".format(curr.timestamp, curr.data))
                curr = curr.next
        pass




blockchain = Blockchain()

#Test insert block with same timestamp
blockchain.add_block(100)
blockchain.add_block(200)

#Test insert empty data
time.sleep(.5)
blockchain.add_block()

time.sleep(.8)
blockchain.add_block(400)
time.sleep(1)
blockchain.add_block(500)

blockchain.print()




