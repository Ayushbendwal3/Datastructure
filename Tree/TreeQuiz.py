class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def printTree(self, printby=None):
        self.printby = printby
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|-->" if self.parent else ""
        if printby == "name":
            value = self.name
        elif printby == "designation":
            value = self.designation
        else:
            value = self.name + " (" + self.designation+")"

        print(prefix+value)
        if self.children:
            for child in self.children:
                child.printTree(printby)


if __name__ == "__main__":
    principal = TreeNode("R.S. Tare", "principal")
    csHOD = TreeNode("Vijay Bircha", "CSHOD")
    teacher = TreeNode("Karishma Mandloi", "Teacher")
    student = TreeNode("Ayush Bendwal", "Student")

    principal.add_child(csHOD)
    csHOD.add_child(teacher)
    teacher.add_child(student)

    principal.printTree()
