class General:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def display(self):
        print(self.data)


class QueueArray(General):
    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.isEmpty():
            print("Queue is empty.")
        return self.data.pop(0)


class DequeArray(General):
    def addFirst(self, e):
        self.data.insert(0, e)

    def addLast(self, e):
        self.data.append(e)

    def removeFirst(self):
        if self.isEmpty():
            return 'DEQueue is Empty.'
        return self.data.pop(0)

    def removeLast(self):
        if self.isEmpty():
            return 'DEQueue is Empty.'
        return self.data.pop(-1)

    def first(self):
        if self.isEmpty():
            return 'DEQueue is Empty.'
        return self.data[0]

    def last(self):
        if self.isEmpty():
            return 'DEQueue is Empty.'
        return self.data[-1]


dq = DequeArray()
dq.addFirst(42)
dq.addFirst(36)
dq.display()
print(dq.removeFirst())
dq.display()