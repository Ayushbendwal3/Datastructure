class TreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1

        return level

    def printTree(self, lvl):
        if self.get_level() > lvl:
            return lvl

        spaces = " " * self.get_level() * 2
        prefix = spaces + "|-->" if self.parent else ""
        print(prefix+self.name)
        if self.children:
            for child in self.children:
                child.printTree(lvl)


if __name__ == "__main__":
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")
    newjersey = TreeNode("New Jersey")
    newjersey.add_child(TreeNode("Princeton"))
    newjersey.add_child(TreeNode("Trenton"))
    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Altp"))
    usa.add_child(newjersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    root.printTree(3)
