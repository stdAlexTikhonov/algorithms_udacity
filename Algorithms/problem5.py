class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixies(self, suffix = ''):
        my_list = []
        for k,v in self.children.items():

            for el in list_words(v):
                if suffix in k + el:             
                    my_list.append(k+el)

            if v.is_word and suffix in k:
                my_list.append(k)

        return my_list  
        

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return -1
            current_node = current_node.children[char]
            
        return current_node

word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.insert(word)

def list_words(trie):
    my_list = []
    for k,v in trie.children.items():

        for el in list_words(v):             
            my_list.append(k+el)

        if v.is_word:
            my_list.append(k)

    return my_list

# Test words
test_pref = ['a', 'z', 'go']
for pref in test_pref:
    node = word_trie.find(pref)
    if node != -1:
        print(node.suffixies())
    else:
        print(node)

# Inserting a key into Trie is a simple approach. 
# Every character of the input key is inserted as an individual Trie node. Note that the children is an array of pointers (or references) to next level trie nodes.
# The key character acts as an index into the array children. If the input key is new or an extension of the existing key, we need to construct non-existing nodes of the key, and mark end of the word for the last node.
# If the input key is a prefix of the existing key in Trie, we simply mark the last node of the key as the end of a word.
# The key length determines Trie depth. 