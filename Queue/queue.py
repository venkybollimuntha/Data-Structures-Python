from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):

        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer) ==0:
            print("Queue is Empty")
            return 
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

q = Queue()

def producers(arr):
    for a in arr:
        print("Placing order for order",a)
        q.enqueue(a)
        time.sleep(0.2)


def consumers():
    time.sleep(1)
    while True:
        order = q.dequeue()
        if order is None:
            break
        print("Now serving order", order)

arr = ['pizza','samosa','pasta','biryani','burger']
threading.Thread(target = producers, args = (arr,)).start()
threading.Thread(target = consumers).start()
print("Done")
