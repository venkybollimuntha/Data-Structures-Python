class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        if self.head is None:
            self.head = Node(data,self.head,None)
            return

        node = Node(data,self.head,None)
        self.head.prev = node # first we have to assign prev value
        self.head = node # then head value.


    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr) # Here you must pass itr (self.head)
        # as the value, otherwised backward print won't get all 

    def get_length(self):
        c = 0
        itr = self.head
        while itr:
            itr = itr.next
            c +=1

        return c

    def insert_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Index out of bounds")

        itr = self.head
        c = 0
        while itr:
            if c == index -1:
                node = Node(data,itr.next,itr)
                itr.next = node
                break
            c+=1
            itr = itr.next

    def remove_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Index out of bounds")

        itr = self.head
        c = 0
        while itr:
            if c == index -1:
                itr.next = itr.next.next
                break
            c+=1
            itr = itr.next

    def remove_by_value(self,data):
        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_after_value(self,index_val,insert_val):
        itr = self.head
        while itr:
            if itr.data == index_val:
                node = Node(insert_val,itr.next,itr)
                itr.next = node
                break
            itr = itr.next


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_values(["banana","mango","grapes","orange"])
    dll.insert_at_begining(10)
    dll.insert_at_begining(20)
    dll.insert_at_begining(30)
    dll.insert_at_begining(40)
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(3,"Venky")
    dll.print_forward()
    dll.remove_at(3,"Venky")
    dll.print_forward()
    dll.remove_by_value(10)
    dll.print_forward()
    dll.insert_after_value('banana',"Apple")
    dll.print_forward()
    dll.print_backward()
