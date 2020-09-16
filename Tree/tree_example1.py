class TreeNode:
    def __init__(self,name,designition=None):
        self.name = name
        self.designition = designition
        self.children = [] # This children is the instance to next class
        self.parent = None

    def add_child(self, child):
        self.children.append(child) # Adding new children object.
        child.parent = self  # Assigning parent to children object.
        # we CANNOT add like this
        # child.parent = self.children.append(child)

    def print_tree(self,typ=None):
        space = "   " * self.get_level()
        if typ == "name":
            print(space + "|--"+ self.name)
        elif typ == "designition":
            print(space + "|--"+ self.designition)
        else:
            print(space + "|--" + self.name + " (" + self.designition+ ")")
        
        if self.children:
            for child in self.children:
                child.print_tree(typ=typ)

    def get_level(self):
        level = 0
        p = self.parent # parent object will give the levels or hirarchey.
        while p:
            level +=1
            p = p.parent
        return level

def build_product_tree():
    root = TreeNode("Nilpul","CEO")

    cto = TreeNode("Chinmay","CTO")
    ih = TreeNode("Vishwa",'Infrastructure Head')
    ih.add_child(TreeNode("Dhaval",'Cloud Manager'))
    ih.add_child(TreeNode("Abhijit",'App Manager'))
    cto.add_child(ih)

    cto.add_child(TreeNode("Aamir","Application Head"))

    hr = TreeNode("Gels",'HR Head')
    hr.add_child(TreeNode('Peter','Recruitment Manager'))
    hr.add_child(TreeNode('waqas','Policy Manager'))

    root.add_child(cto)
    root.add_child(hr)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree(typ= "designition")
    root.print_tree(typ= "name")
    root.print_tree()
