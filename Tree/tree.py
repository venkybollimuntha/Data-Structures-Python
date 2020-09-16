class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = [] # This children is the instance to next class
        self.parent = None

    def add_child(self, child):
        self.children.append(child) # Adding new children object.
        child.parent = self  # Assigning parent to children object.
        # we CANNOT add like this
        # child.parent = self.children.append(child)

    def print_tree(self):
        space = "   " * self.get_level()
        print(space + "|--"+ self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent # parent object will give the levels or hirarchey.
        while p:
            level +=1
            p = p.parent
        return level

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop") 
    asus = TreeNode('Asus')
    asus.add_child(TreeNode("Vivobooks14"))
 
    laptop.add_child(asus)
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Microsoft'))

    mobile = TreeNode("Mobile")

    mobile.add_child(TreeNode('Xioami'))
    mobile.add_child(TreeNode('Oppo'))
    mobile.add_child(TreeNode('Samsung'))
    mobile.add_child(TreeNode('Iphone'))

    tv = TreeNode("Television")

    tv.add_child(TreeNode('Sony'))
    tv.add_child(TreeNode('MI'))
    tv.add_child(TreeNode('OnePlus'))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(mobile)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
