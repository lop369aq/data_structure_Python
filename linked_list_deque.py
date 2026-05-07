class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class Linkedlistdeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        
    def push_front(self, data):

        new_node = node(data)
        
        if self.front == None:
            self.front = self.rear = new_node
            
        else:
            self.front.left = new_node
            new_node.right = self.front
            self.front = new_node
        
        self.count = self.count + 1

        return "PUSH_FRONT_SUCCESS"
    
    def push_rear(self, data):

        new_node = node(data)
        if self.rear == None:
            self.rear = self.front = new_node
            
        else:
            self.rear.right = new_node
            new_node.left = self.rear
            self.rear = new_node

        self.count = self.count + 1
        return "PUSH_REAR_SUCCESS"
    
    def is_empty(self):
        if self.count == 0:
            print("deque is empty")
            
            
        else:
            return "="*5 +'''deque is not empty, node_count: %d''' %self.count + "="*5 
            

    def pop_front(self):
        
        if self.count == 0:
            print("deque is empty")

        elif self.count == 1:
            data = self.front.data
            self.front = self.rear = None
            self.count = self.count - 1
            return "pop data = %d" %data
        
        else:
            data = self.front.data
            self.front.right.left = None
            self.front = self.front.right
            self.count = self.count -1
            return "pop data = %d" %data
            
    
    def pop_rear(self):

        if self.count == 0:
            print("deque is empty")
        
        elif self.count == 1:
            data = self.rear.data
            self.rear = self.front = None
            self.count = self.count -1
            return "pop data = %d" %data
        
        else:
            data = self.rear.data
            self.rear.left.right = None
            self.rear = self.rear.left
            self.count = self.count -1
            return "pop data = %d" %data
        
    def peek(self):
        front_or_rear = int(input("front:0 or rear:1 :"))

        if front_or_rear == 0 and self.count != 0:
            data = self.front.data
            return "peek front data = %d" %data
        elif front_or_rear == 1 and self. count != 0:
            data = self.rear.data
            return "peek rear data = %d" %data
            
        else:
            return "Error"


deque = Linkedlistdeque()

print(deque.push_front(1))
print(deque.push_front(2))
print(deque.push_front(2))
print(deque.push_front(2))
print(deque.push_front(2))

print(deque.is_empty())