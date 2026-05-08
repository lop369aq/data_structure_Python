class circle_arrayqueue:

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = capacity
        self.count = 0
    
    def enqueue(self, data):

        if self.queue[self.rear] != None:
            return "queue is full"
        
        else:
            self.queue[self.rear] = data
            self.count = self.count + 1
            self.rear = self.rear + 1
            
            if self.rear == self.size:
                self.rear = 0

            return "SUCCESS"
    
    def dequeue(self):
        if self.queue[self.front] == None:
            return "queue is empty"
        
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.count = self.count - 1
            self.front = self.front + 1
            if self.front == self.size:
                self.front = 0
            return data
        
    def full_or_empty(self):
        if self.count == 0:
            return "queue is empty"
        elif 1 <= self.count and self.count < self.size:
            return "queue is not full"
        else:
            return "queue is full"
    
    def queue_check(self):
        result = []
        for _ in range(self.count):
            result.append(self.queue[self.front])
            self.front = self.front + 1

            if self.front == self.size:
                self.front = 0
        return result



queue = circle_arrayqueue(5)

print(queue.enqueue(1))
print(queue.enqueue(2))
print(queue.enqueue(3))
print(queue.enqueue(4))
print(queue.enqueue(5))

print(queue.queue_check())

print(queue.dequeue())

print(queue.queue_check())
print(queue.enqueue(6))
print(queue.queue_check())
print(queue.dequeue())








            
