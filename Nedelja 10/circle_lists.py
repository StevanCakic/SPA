class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None 

    def prepend(self, new_node):
        cur = self.head 
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, new_node):
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node = new_node
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    # pretpostavljamo da nema duplikata!
    def remove(self, key):
        if self.head.data == key:
            cur = self.head 
            while cur.next != self.head:
                cur = cur.next 
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head 
            prev = None 
            while cur.next != self.head:
                prev = cur 
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next 
                    cur = cur.next

    def print_list(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


cllist = CircularLinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

cllist.append(node3)
cllist.append(node4)
cllist.prepend(node2)
cllist.prepend(node1)
cllist.print_list()

print("---------------")
cllist.remove(1)
cllist.remove(5)
cllist.print_list()