class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def get_tail(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        return temp

    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\r")

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_tail()
        temp = last_node
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print("\r")

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        last_node = self.get_tail()
        node = Node(data, next=None, prev=last_node)
        last_node.next = node

    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        return count

    def insertHead(self, data):
        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node

    def insert_values(self, data_list):
        self.head = None
        for i in data_list:
            self.append(i)

    def removeAt(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        temp = self.head
        count = 0
        while temp:
            if count == index:
                temp.prev.next = temp.next

                if temp.next:
                    temp.next.prev = temp.prev
                break

            temp = temp.next
            count += 1

    def insertAt(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insertHead(data)
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(data, next=temp.next, prev=temp)
                if node.next:
                    node.next.prev = node
                temp.next = node
                break

            temp = temp.next
            count += 1

    def insert_after_value(self, data_after, data):
        if self.head is None:
            return

        temp = self.head
        while temp:
            if temp.data == data_after:
                temp.next = Node(data, next=temp.next, prev=temp)
                break

            temp = temp.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        temp = self.head

        while temp:
            if temp.data == data:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

            temp = temp.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(100)
    dll.append(101)
    dll.append(102)
    dll.insertHead(99)
    dll.print_forward()
    dll.insert_after_value(99, 99.5)
    dll.print_forward()
    dll.remove_by_value(101)
    dll.print_forward()
