class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element):
        self._element = element
        self._next = None

    @property
    def element(self):
        return self._element

    @property
    def next(self):
        return self._next


class LinkedList:
    __slots__ = 'elements', 'head', 'tail', 'size'

    def __init__(self, element):
        self.elements = element
        self.head = _Node(element)
        self.tail = self.head
        self.size = 1

    def __len__(self):
        return self.size

    def addLast(self, element):
        newest = _Node(element)
        self.tail._next = newest
        self.tail = newest
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def printLink(self):
        x = self.head
        while x:
            print(x.element)
            x = x.next

    def addAny(self, e, position):
        newest = _Node(e)
        p = self.head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        newest._next = p.next
        p._next = newest
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            print("Linked List is Empty")
            return
        e = self.head._element
        self.head = self.head._next
        self.size -= 1
        if self.isEmpty():
            self.tail = None
        return e

    def removeAny(self, position):
        p = self.head
        i = 1
        while i < position-1:
            p = p._next
            i += 1
        remove = p._next
        p._next = remove._next
        self.size -= 1
        return remove._element


l1 = LinkedList(7)
l1.addLast(12)
l1.addLast(13)
l1.printLink()
