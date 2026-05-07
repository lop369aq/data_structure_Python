class ArrayStack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def item_push(self, item):

        if self.top + 1 == self.capacity:
            print("이미 스텍이 전부 차있습니다.")
            raise Exception("Stack is full")
        else:
            self.top = self.top + 1
            self.stack[self.top] = item
            print("%d원소에 정상적으로 입력되었습니다." %self.top)
    
    def item_pop(self):
        
        if self.top == -1:
            print("스텍이 비어있습니다.")
            raise Exception("stack is empty")
        else:
            data = self.stack[self.top]
            self.top = self.top -1
            print("정상적으로 pop완료.")
            return data
        
    def peek(self):
        if self.top == -1:
            print("스텍이 비어있습니다.")
            return
        else:
            item = self.stack[self.top]
            return item

stack = ArrayStack(5)

stack.item_push(5)
stack.item_push(4)
stack.item_push(3)
stack.item_push(2)
stack.item_push(2)



print(stack.peek())
