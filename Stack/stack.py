from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        try:
            return self.container[-1]
        except IndexError:
            return ''

    def is_empty(self):
        return len(self.container) ==0

    def size(self):
        return len(self.container)

    def print(self):
        return print(self.container)

    def reverse(self,val):
        self.container.append(val) 
        return self.pop()[::-1]
        
if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.print()
    s.reverse()
