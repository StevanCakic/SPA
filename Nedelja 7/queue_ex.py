class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueue(self, item):
        self.size += 1
        return self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            self.size -= 1
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def first(self):
        if not self.is_empty():
            return self.items[0]

    def get_queue(self):
        return self.items

    def __len__(self):
        return len(self.items)

q = Queue()

print(q.is_empty())

q.enqueue("Wake up")
q.enqueue("Have a caffee")
q.enqueue("Have a shower")
q.enqueue("Get dress")
q.enqueue("Go to breakfast")
q.enqueue("Go to faculty")

q.dequeue()