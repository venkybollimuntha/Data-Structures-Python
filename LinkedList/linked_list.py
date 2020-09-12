class Node:
    def __init__(self, data = None, next= None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head
        # itr.next will gives the last element, we can insert value here.
        while itr.next:
            itr = itr.next # This value becomes None, but we are checking itr.next value.

        itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        mystr = ''
        # itr checks the value until the end. By default last value is None and loop breaks.
        while itr:
            mystr += str(itr.data) + "-->"
            itr = itr.next
        print(mystr)
        return

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        print(count)
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Index Not found')

        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next

            count +=1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Index Not found')

        if index ==0:
            self.insert_at_begining(data)

        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1
            
    def insert_values(self,data):
        for d in data:
            self.insert_at_end(d)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr.next:
            """
            if we want to carry previous nodes then chek with itr.next in 
            while loop
            """
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


# Driver code
ll = LinkedList()

ll.insert_at_end(30)
ll.insert_at_end(400)
ll.insert_at_begining(10)
ll.insert_at_begining(18)
ll.insert_at_end(50)
ll.print()
ll.remove_at(3)
ll.print()
ll.insert_at(3,"Hello")
ll.print()
ll.get_length()
