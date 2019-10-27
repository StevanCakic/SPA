class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def prepend(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if not self.head: 
            return None
        # Move the head pointer to the next node 
        self.head = self.head.next

    def delete_last(self):
        temp = self.head
        while temp.next:
            prev  = temp
            temp = temp.next
        prev.next = None

    def get_from_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert_on_position(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete_val(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def delete_from_pos(self, pos):
        current = self.head
        if pos == 0:
            self.head = current.next
            current = None
            return
        
        previous = None
        count = 1

        while current and count != pos:
            previous = current
            current = current.next
            count += 1

        if current is None:
            return

        previous.next = current.next
        current = None
    
    def len_iterative(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.print_list()
print("-------------")

ll.prepend(Node(5))
ll.print_list()
print("-------------")

ll.delete_first()
ll.print_list()
print("-------------")

ll.delete_last()
ll.print_list()
ll.append(e3)
print("-------------")

# Test get_node_from_position
print(ll.head.next.next.value)
print("-------------")

# Should also print 3
print(ll.get_from_position(3).value)
print("-------------")

# Test insert
ll.insert_on_position(e4,3)
# Should print 4 now
print(ll.get_from_position(3).value)
print("-------------")
ll.print_list()
print("-------------")

'''
# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_from_position(1).value)
# Should print 4 now
print(ll.get_from_position(2).value)
# Should print 3 now
print(ll.get_from_position(3).value)
'''