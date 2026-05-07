class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = node(data)

        if self.head == None:
            self.head = self.tail = new_node
        
        else :
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
    def insert_at_tail(self, data):
        new_node = node(data)
        if self.tail == None:
            self.head = self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    def delete_from_head(self):
        if not self.head:
            print("노드가 존재하지 않습니다.")
            return
        
        elif self.head == self.tail:
            self.head = self.tail = None

        else : 
            self.head = self.head.next
            self.head.prev = None

    def delete_from_tail(self):
        if not self.tail:
            print("노드가 존재하지 않습니다.")
        elif self.tail == self.head:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def search_from_head(self, key):
        i = 0
        current = self.head

        if not self.head :
            print("노드가 존재하지 않습니다.")
            return
        elif self.head == self.tail:
            if self.head.data == key:
                print("0번째 노드에 있습니다.")
                return
            else :
                print("현재 데이터가 존재하지 않습니다.")
                return
        else :
            while True :
                if current.data == key:
                    print("%d번째 노드에 존재합니다." %i)
                    return
                current = current.next
                if not current :
                    print("데이터가 존재하지 않습니다.")
                    return
                i = i+1
    def search_from_tail(self, key):
        i = 0
        current = self.tail

        while True:
            if not self.tail :
                print("노드가 존재하지 않습니다.")
                return
            
            elif self.head == self.tail:
                if self.tail.data == key:
                    print("0번째 노드에 있습니다.")
                    return
                else :
                    print("현재 데이터가 존재하지 않습니다.")
                    return
                
            else :
                while True :
                    if current.data == key:
                        print("%d번째 노드에 존재합니다." %i)
                        return
                    
                    current = current.prev

                    if not current :
                        print("데이터가 존재하지 않습니다.")
                        return
                    i = i+1
    # def traverse_from_head(self):
        
                    
                    



    
