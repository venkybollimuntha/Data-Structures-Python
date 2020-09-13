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

    def is_balanced(self,str_val):
    """
    This logic is written by me
    """

        for char in str_val:

            if char == "{"  or char == '(' or char == '[':
                self.container.append(char)

            if char == ")":
                if self.peek() == "(":
                    self.container.pop()
                else:
                    return False

            if char == "}":
                if self.peek() == "{":
                    self.container.pop()
                else:
                    return False

            if char == ']':
                if self.peek() == '[':
                    self.container.pop()
                else:
                    return False
                    
        return len(self.container) ==0

    def clear(self):
        return self.container.clear()

stack = Stack()

print(stack.is_balanced("{a+b}"))
stack.clear()
print(stack.is_balanced("))((a+b}{"))
stack.clear()
print(stack.is_balanced("((a+b))"))
stack.clear()
print(stack.is_balanced("))"))
stack.clear()
print(stack.is_balanced("[a+b]*(x+2y)*{gg+kk}"))
