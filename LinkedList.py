class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # make the tail next ptr point at the new node
        self.tail.next = new_node

        # make the tail point at the new node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def delete(self, item):
        prev_song = self.head
        current = self.head

        if current.data == item:
            self.head = self.head.next

        while current.data != item:
            prev_song = current
            current = current.next

        if current.data == item:
            next_item = current.next
            prev_song.next = next_item

    def find(self):
        pass

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next
