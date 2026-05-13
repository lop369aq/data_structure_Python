# array_deque(unoptimized)



class circle_array_deque:

    def __init__(self, capacity):

        self.deque = [None] * capacity
        self.size = capacity

        self.front = 0
        self.rear = -1
        self.count = 0

    def push_front(self, data):

        if self.deque[self.front] == None:
            self.deque[self.front] = data
            self.front = self.front + 1
            self.front = self.front % self.size
            self.count = self.count + 1
            return "Success"

        else:
            return "Can't Push"

            
    def push_rear(self, data):

        if self.deque[self.rear] == None:

            self.deque[self.rear] = data
            self.count = self.count + 1
            self.rear = self.rear -1

            if self.rear == -(self.size) - 1:
                self.rear = -1

            return "Success"
            
        else:
            return "Can't Push"
    
    def pop_front(self):
        if self.front == 0:
            self.front = self.size - 1
            if self.deque[self.front] == None:
                self.front = 0
                return "Can't pop" 
            else:
                data = self.deque[self.front]
                self.deque[self.front] = None
                self.count = self.count - 1
                return data
        else:
            self.front = self.front - 1
            if self.deque[self.front] == None:
                self.front = self.front + 1
                return "Can't pop"
            else:
                data = self.deque[self.front]
                self.deque[self.front] = None
                self.count = self.count - 1
                return data

    def pop_rear(self):
        if self.rear == -1:

            self.rear = 0
            
            if self.deque[self.rear] == None:
                self.rear = -1
                return "Can't pop" 
            else:
                data = self.deque[self.rear]
                self.deque[self.rear] = None
                self.rear = -(self.size)
                self.count = self.count - 1
                return data
        
        else:
            self.rear = self.rear + 1
            if self.deque[self.rear] == None:
                self.rear = self.rear - 1
                return "Can't pop"
            else:
                data = self.deque[self.rear]
                self.deque[self.rear] = None
                self.count = self.count - 1
                return data
        
            

    def is_empty(self):

        if self.count == 0:
            return "deque is empty"
        
        else:
            return "deque is not empty"
    
    def data_count(self):
        return self.count
    
# deque = circle_array_deque(6)

# print(deque.push_front(5))
# print(deque.push_front(4))
# print(deque.push_front(3))
# print(deque.push_front(2))
# print(deque.push_front(1))
# print(deque.push_front(0))
# print(deque.push_front(0))
# print(deque.pop_front())
# print(deque.pop_front())
# print(deque.pop_front())
# print(deque.pop_rear())
# print(deque.pop_rear())
# print(deque.pop_rear())
# print(deque.pop_rear())
# print(deque.is_empty())
# print(deque.push_front(0))
# print(deque.is_empty())
