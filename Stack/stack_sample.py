class Stack:
    def __init__(self):
        self.container = deque()

    def add(self,val):
        self.container.append(val)

    def remove(self):
        self.container.pop()

    def show(self):
        return list(self.container)

s = Stack()
s.add(10)
s.add(20)
s.add(30)
s.add(40)
print(s.show())
s.remove()
s.remove()
print(s.show())
