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
            return self.items[0].data
    def __len__(self):
        return len(self.items)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder(self.root, "")
        else:
            return ("Invalid traversal type")
    
    def preorder(self, start, traversal):
        # start -> self.root
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    
    def inorder(self, start, traversal):
        # start -> self.root
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal
    
    def postorder(self, start, traversal):
        # start -> self.root
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal

    def levelorder(self, start, traversal):
        if start is None:
            return 
        queue = Queue()
        queue.enqueue(start)

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal


bin_tree = BinaryTree(6)
bin_tree.root.left = Node(3)
bin_tree.root.right = Node(7)
bin_tree.root.left.left = Node(2)
bin_tree.root.left.right = Node(5)
bin_tree.root.right.right = Node(9)
print(bin_tree.print_tree("preorder"))
print(bin_tree.print_tree("inorder"))
print(bin_tree.print_tree("postorder"))
print(bin_tree.print_tree("levelorder"))
