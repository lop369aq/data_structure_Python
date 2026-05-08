class node:
    def __init__(self, data):
        self.data = data
        self.prev = None

class liststack:

    def __init__(self):
        self.pointer = None
        self.count = 0

    def push(self, data):
        new_node = node(data)
        new_node.prev = self.pointer
        self.pointer = new_node
        self.count = self.count + 1
    
    def pop(self):
        if self.pointer == None:
            raise Exception("stack is empty")
        else:
            data = self.pointer.data
            self.pointer = self.pointer.prev
            self.count = self.count - 1
            return data
        
    def peek(self):
        if self.pointer == None:
            raise Exception("stack is empty")
        else:
            return self.pointer.data
        
    def stack_count(self):
        return self.count
    
    def is_empty(self):
        return self.count == 0
    
