class RouteTrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.handler = None
        self.children = {}
    
    def insert(self, route):
        self.children[route] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        path = path.split('/')

        current_node = self.root
        for word in path:
            if word not in current_node.children:
                current_node.insert(word)
            current_node = current_node.children[word]
            
        current_node.handler = handler

    def find(self, path):
        ## Find the Trie node that represents this prefix
        path = path.split('/')

        current_node = self.root
        
        for word in path:
            if word not in current_node.children:
                return -1
            current_node = current_node.children[word]
            
        return current_node.handler


router = RouteTrie()

router.insert('/home', 'home handler')
router.insert('/about', 'about handler')
router.insert('/about/me', 'about me handler')
router.insert('/about/data', 'about data handler')
router.insert('/about/data/test', 'about test handler')
router.insert('/about/data/cupture', 'about cupture handler')

test_list = ['/home', '/about','/about/me','/about/data','/about/data/test','/about/data/cupture', '']

for word in test_list:
    print(router.find(word))
