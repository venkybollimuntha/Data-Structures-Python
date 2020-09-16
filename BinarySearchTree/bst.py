class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


    def add_child(self,data):
        if self.data == None: # if main node is empty add directly
            self.data = data

        if data < self.data: # Add data in the left subtree
            if self.left:
                self.left.add_child(data) # adding left side
            else: # left subtree is None add directly
                self.left = BinarySearchTreeNode(data)

        if data > self.data: # Add data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        """
        In order traversal means traversing from
        left to main node and then right node.
        precisely, asending order.
        """
        elements = []
        # visit the left tree first
        if self.left:
            # recursively traversing each node in left side.
            elements += self.left.in_order_traversal()


        # visit the main node next
        elements.append(self.data)

        # visit the right node next
        if self.right:
            # recursively traversing each node in right side.
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
    	elements = []

    	if self.left:
    		elements += self.left.post_order_traversal()

    	if self.right:
    		elements += self.right.post_order_traversal()

    	elements.append(self.data)

    	return elements

    def pre_order_traversal(self):
    	elements = [self.data]

    	if self.left:
    		elements += self.left.pre_order_traversal()

    	if self.right:
    		elements += self.right.pre_order_traversal()

    	return elements


    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    elements = [17,2,3,4,1,20,50,6,7,8,9]
    numbers_tree = build_tree(elements)

    # out put have two utilities:
    # Implement tree and Sort the elements in the list
    # Set like implementation, No duplicates allowed.
    print(numbers_tree.in_order_traversal())

    print(numbers_tree.search(2))
