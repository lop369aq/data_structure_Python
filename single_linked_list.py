class node:
    def __init__(self, data) :
        self.data = data
        self.next = None

class admin:

    def __init__(self):
        self.head = None
    
    def head_create(self, data):
        created_node = node(data)
        created_node.next = self.head
        self.head = created_node
    
    def insert_node(self, data, position):

        new_node = node(data)
        current_node = self.head

        if position == 0:
                self.head_create(data)
                return
        
        if self.head != None :

            for _ in range(position-1): #범위를 벗어난 경우 판별하기

                if current_node == None:
                    return
                current_node = current_node.next
            
            if current_node == None : #끝노드
                return
            
            new_node.next = current_node.next
            current_node.next = new_node
    
    def delete(self, key):

        current = self.head
        prev = None

        while current :

            if key == current.data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return 
            prev = current
            current = current.next
        print("삭제할 값이 존재하지 않습니다.")
    
    def search(self, key):
        current = self.head
        i = 0
        while current:
            if key == current.data:
                print("%d번째 노드에서 발견." %i)
                return
            current = current.next
            i = i + 1
        print("어떤 노드에도 존재하지 않습니다.")
    
    def traverse(self):
        i = 0
        current = self.head
        while current:
            print("%d번째 노드의 값은 %d입니다." %(i, current.data))
            i = i + 1
            current = current.next
        print("끝 노드까지 순회를 완료하였습니다.")

single_list = admin()

single_list.head_create(17)
single_list.head_create(18)
single_list.head_create(19)
single_list.head_create(20)
single_list.head_create(21)

single_list.insert_node(31,3)

single_list.traverse()






            
        

        

            
            




        
            
            




