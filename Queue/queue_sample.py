from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def add(self,val):
        self.buffer.append(val)

    def remove(self):
        return self.buffer.popleft()

    def show(self):
        return list(self.buffer)


q = Queue()

q.add(10)
q.add(20)
q.add(30)
q.add(40)
q.add(50)
q.add(60)
print(q.show())
q.remove()
q.remove()
print(q.show())
