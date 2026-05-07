class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlistqueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front == None:
            new_node = node(data)
            self.front = self.rear = new_node
            return "enqueue Success"
        else:
            new_node = node(data)
            self.rear.next = new_node
            self.rear = new_node
            return "enqueue Success"
    
    def dequeue(self):
        if self.front == None:
            return "Queue is empty"
        
        else:
            data = self.front.data
            self.front = self.front.next
            return data

    def check_empty(self):
        if self.front == None:
            return "Queue is empty"
        else:
            return "queue is not empty"
        
    def display(self):
        i = self.front
        while(i != None):
            print(i.data)
            i = i.next

q = linkedlistqueue()

print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
q.display()

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.check_empty())

print(q.enqueue(1))
print(q.check_empty())
q.display()


