class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def get_tail(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        return temp

    def insertHead(self, data):
        node = Node(data, self.head)
        self.head = node

    def append(self, data):
        temp = self.head

        if temp is None:
            node = Node(data, None)
            self.head = node
            return node

        while temp.next:
            temp = temp.next

        temp.next = Node(data, None)

    def printList(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        llstr = ''

        while temp:
            llstr += str(temp.data) + '--->'
            temp = temp.next

        print(llstr)

    def insert_values(self, data_list):
        self.head = None
        for i in data_list:
            self.append(i)

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        return count

    def removeAt(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next

            temp = temp.next
            count += 1

    def pop(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            return None

        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None

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
                node = Node(data, temp.next)
                temp.next = node

            temp = temp.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)

        temp = self.head
        while temp:
            if temp.data == data_after:
                temp.next = Node(data_to_insert, temp.next)
                break

            temp = temp.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                break

            temp = temp.next

    def reverse(self):
        if self.head is None:
            return None

        prev = None
        temp = self.head

        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    def ispalindrome(self):
        temp = self.head
        s = ''
        while temp:
            s += str(temp.data)
            temp = temp.next

        revs = s[::-1]
        if s == revs:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    ll = LinkedList()
    list1 = [1,2,1]
    ll.insert_values(list1)
    ll.printList()
    ll.insert_after_value(2, 2.5)
    ll.printList()
    ll.remove_by_value(2.5)
    ll.printList()
    ll.ispalindrome()
