class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class dll_Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
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
        prev = self.head
        current = self.head

        if current.data == item:
            self.head = self.head.next

        while current.data != item:
            prev = current
            current = current.next

            if current == None:
                return -1

            if current.data == item:
                next_item = current.next
                prev.next = next_item

    def find(self, item):
        '''Find a specific item in the linked list, return the node, if not found return None'''
        current = self.head
        itemFound = False

        while current != None:
            if item == current.data:
                itemFound = True
                return current

            current = current.next

        if itemFound == False:
            return None

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


class DoublyLinkedList:
    def __init__(self):
        self.next = None
        self.prev = None
        self.head = None

    def dll_append(self, data):
        new_node = dll_Node(data)
        last = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last.next = new_node
        new_node.prev = last

    def dll_print(self):
        node = self.head
        last = None
        print("List forwards ")
        while (node != None):
            print(node.data)
            last = node
            node = node.next

        print("\nList backwards ")
        while (last != None):
            print(last.data)
            last = last.prev

    def dll_prepend(self, data):
        node = self.head
        new_node = dll_Node(data)
        new_node.next = self.head
        self.head = new_node
        node.prev = new_node

        return
