# Inserting a key into Trie is a simple approach.

# Every character of the input key is inserted as an individual Trie node. Note that the children is an array of pointers (or references) to next level trie nodes.

# The key character acts as an index into the array children. If the input key is new or an extension of the existing key, we need to construct non-existing nodes of the key, and mark end of the word for the last node.

# If the input key is a prefix of the existing key in Trie, we simply mark the last node of the key as the end of a word.

# The key length determines Trie depth.

# Insert

Time complexity: O(h) where h is height of the BST
Space complecity: O(n)

# Find

Time complexity: O(h) where h is height of the BST
Space complecity: O(n)
