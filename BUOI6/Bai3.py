class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.capacity

    def top(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def push(self, value):
        if not self.isFull():
            self.items.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()


stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)

print(stack1.isFull())  
print(stack1.top())     
print(stack1.pop())     
print(stack1.top())     
