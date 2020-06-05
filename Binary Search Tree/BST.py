class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def postOrder(self):
        elements = []

        if self.left:
            elements += self.left.postOrder()

        if self.right:
            elements += self.right.postOrder()

        elements.append(self.data)

        return elements

    def preOrder(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.preOrder()

        if self.right:
            elements += self.right.preOrder()

        return elements

    def search(self, value):
        if self.data == value:
            return True

        if self.data > value:
            if self.left:
                return self.left.search(value)
            else:
                return False

        if self.data < value:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def inOrder(self):
        elements = []

        if self.left:
            elements += self.left.inOrder()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrder()
        return elements

    def sum(self):
        left_sum = self.left.sum() if self.left else 0
        right_sum = self.right.sum() if self.right else 0
        return self.data + left_sum + right_sum

    def find_max(self):
        if self.right is None:
            return self.data

        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

    def addChild(self, data):
        if data == self.data:
            return

        if data < self.data:

            if self.left:
                self.left.addChild(data)

            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.addChild(data)

            else:
                self.right = BinarySearchTreeNode(data)

    def deleteNode(self, value):
        if self.data > value:
            if self.left:
                self.left = self.left.deleteNode(value)

        elif self.data < value:
            if self.right:
                self.right = self.right.deleteNode(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.deleteNode(max_value)

        return self


def buildTree(elements):
    root = tree = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root


if __name__ == "__main__":

    number = [121, 54, 231, 56, 123, 564, 234, 54, 23, 455]
    tree = buildTree(number)
    print(tree.inOrder())
    tree.deleteNode(121)
    print(tree.inOrder())
