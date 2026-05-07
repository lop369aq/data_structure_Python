class circle_array_deque:

    def __init__(self, capacity):

        self.deque = [None] * capacity
        self.size = capacity

        self.front = 0
        self.rear = -1
        self.count = 0

    def push_front(self, data):

        if self.deque[self.first] == None:
            self.deque[self.first] == data
            self.first = self.first + 1
            self.first = self.first % self.size
            self.count = self.count + 1

        else:
            return "Can't Push it"

            
    def push_rear(self, data):

        if self.deque[self.rear] == None:
            self.deque[self.rear] = data
            self.count = self.count + 1
            self.rear = self.rear -1
            if self.rear == -(self.self.size - 1):
                self.rear = self.size - 1
            
        else:
            return "Can't Push it"
    
    def pop_front(self):
        pass

    def pop_rear(self):
        pass

    def is_empty(self):

        if self.count == 0:
            return "deque is empty"
        else:
            return "deque is not empty"
    
    def data_count(self):
        return self.count