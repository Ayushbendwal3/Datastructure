class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|-->" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1

        return level


if __name__ == "__main__":
    principal = TreeNode("Principal")
    CShead = TreeNode("CSHOD")
    EXhead = TreeNode("EXHOD")
    teacher = TreeNode("Teacher")
    student = TreeNode("Student")
    principal.add_child(CShead)
    principal.add_child(EXhead)
    CShead.add_child(teacher)
    teacher.add_child(student)
    principal.printTree()
