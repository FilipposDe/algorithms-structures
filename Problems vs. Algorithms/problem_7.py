# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, home_handler):
        self.root = RouteTrieNode(home_handler)




    def insert(self, path, handler):
        
        node = self.root

        for sub_page in path:

            found_sub_page = node.children.get(sub_page)
            if found_sub_page is None:
                node.insert(sub_page)

            node = node.children[sub_page]

        node.handler = handler




    def find(self, path):
        
        if len(path) == 1 and path[0] == '':
            return self.root.handler
        
        node = self.root

        for sub_page in path:

            found_sub_page = node.children.get(sub_page)
            if found_sub_page is None:
                return None
            
            node  = node.children[sub_page]

        return node.handler







class RouteTrieNode:


    def __init__(self, handler = None):
        self.children = {}
        self.handler = handler


    def insert(self, page_path):
        self.children[page_path] = RouteTrieNode()







class Router:


    def __init__(self, root_handler = "Home Handler", not_found_handler = "404 Handler"):
        self.handler_404 = not_found_handler
        self.route_trie = RouteTrie(root_handler)


    def add_handler(self, path, handler):
        split_path = self.split_path(path)
        self.route_trie.insert(split_path, handler)


    def lookup(self, path):

        split_path = self.split_path(path)

        handler = self.route_trie.find(split_path)

        if handler is None:
            return self.handler_404

        return handler


    def split_path(self, path):

        if path[-1] == '/':
            path = path[:-1]

        return path.split('/')





print('\n\n___________ TEST 1 ___________')

router = Router("root handler", "not found handler")
router.add_handler("/one/two/three", "three handler") 
print(router.lookup("/one/two/three/"))
# Expected: 'three handler'


print('\n\n___________ TEST 2 ___________')

print(router.lookup("/one"))
# Expected: 'not found handler'


print('\n\n___________ TEST 3 ___________')

print(router.lookup("/////"))
# Expected: 'not found handler'



print('\n\n___________ TEST 4 ___________')

# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
