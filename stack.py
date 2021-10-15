class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self.data.append(e)

    def pop(self):
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

    def display(self):
        print(self.data)


s = Stack()
s.push(15)
s.push(25)
s.push(55)
print(s.pop())


