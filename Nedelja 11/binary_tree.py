class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)

    def peek(self):
        if len(self.items) > 0:
            return self.items[0].value
    
    def __len__(self):
        return len(self.items)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # Tree traversal (nacin obilaska drveta)
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root, "")
        
    # DFS - we will do this type of traversal

    # Preorder
    def preorder_print(self, start, traversal):
        # root -> left -> right
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    # Inorder
    def inorder_print(self, start, traversal):
        # left -> root -> right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    # Postorder
    def postorder_print(self, start, traversal):
        # left -> right -> root 
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start, traversal):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    # Insertation
    # Kreirati drvo 8 - 3 - 10 - 1 - 6
    # Kreirati drvo 10 - 8 - 6 - 3 - 1 (Da bi se ovo bolje balansiralo koristi se AVL stablo)
    # Odraditi pretragu kroz drvo
    # 8 - 3 - 10 - 1 - 6 - 9 - 11 (naci 1)
    # Sta ako pretrazujemo 1 u 10 - 8 - 6 - 3 - 1
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.value:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.value:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value is already in tree")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None
    
    def _find(self, data, current_node):
        if data == current_node.value:
            return True
        if data > current_node.value and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.value and current_node.left:
            return self._find(data, current_node.left)

    # Given a non-empty binary search tree, return the node 
    # with minum key value found in that tree. Note that the 
    # entire tree does not need to be searched  
    def min_val_node(self, node): 
        current = node 
    
        # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left  
    
        return current  

    # Given a binary search tree and a key, this function 
    # delete the key and returns the new root 
    def delete_node(self, root, key): 
    
        # Base Case 
        if root is None: 
            return root  
    
        # If the key to be deleted is smaller than the root's 
        # key then it lies in  left subtree 
        if key < root.value: 
            root.left = self.delete_node(root.left, key) 
    
        # If the key to be delete is greater than the root's key 
        # then it lies in right subtree 
        elif(key > root.value): 
            root.right = self.delete_node(root.right, key) 
    
        # If key is same as root's key, then this is the node 
        # to be deleted 
        else: 
            
            # Node with only one child or no child 
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  
                
            elif root.right is None : 
                temp = root.left  
                root = None
                return temp 
    
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree) 
            temp = self.min_val_node(root.right) 
    
            # Copy the inorder successor's content to this node 
            root.value = temp.value 
    
            # Delete the inorder successor 
            root.right = self.delete_node(root.right , temp.value) 
    
        return root

    def get_num_leaf(self, current):
        if not current:
            return 0
        else:
            if not current.left and not current.right:
                return 1
            else:
                return (self.get_num_leaf(current.left) + self.get_num_leaf(current.right))  

bin_tree = BinaryTree(6)
bin_tree.root.left = Node(3)
bin_tree.root.right = Node(7)
bin_tree.root.left.left = Node(2)
bin_tree.root.left.right = Node(5)
bin_tree.root.right.right = Node(9)
#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9

print("Preorder:")
print(bin_tree.print_tree("preorder"))

print("Inorder:")
print(bin_tree.print_tree("inorder"))

print("Postorder:")
print(bin_tree.print_tree("postorder"))

print("Levelorder:")
print(bin_tree.print_tree("levelorder"))

print("Find")
print(bin_tree.find(3))

bin_tree.insert(10)
bin_tree.insert(1)
#          6
#        /   \
#       3     7
#      / \     \
#     2   5     9
#    /           \
#   1            10  
print(bin_tree.print_tree("levelorder"))
bin_tree.delete_node(bin_tree.root, 1)
print(bin_tree.print_tree("levelorder"))
