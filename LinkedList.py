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
        '''Add a new node to the end of the linked list'''
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
        '''Add a new node to the beginning of the linked list'''
        #if self.head is None:
        #    self.head = new_node
        #    self.tail = new_node
        #    return
        new_node = Node(data)
        # Adds new node where the head used to be
        new_node.next = self.head
        self.head = new_node
        return

    def delete(self, item):
        '''Remove a specific data item from the linked list'''
        prev = self.head
        current = self.head

        if current.data == item:
            self.head = self.head.next
        # Traverse linked list
        while current.data != item:
            prev = current
            current = current.next

            if current == None:
                return None
            # If item is found, change the node before's next pointer
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

        # keep going until we hit None at the end of the LL
        while current is not None:
            # print the data of the node we are visiting
            print(current.data)

            # most important piece! move current via reassignment to point at the next node
            current = current.next


class DoublyLinkedList:
    def __init__(self):
        self.next = None
        self.prev = None
        self.head = None

    def dll_append(self, data):
        '''Add a new node to the end of the linked list'''
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
        '''Add a new node to the beginning of the linked list'''
        node = self.head
        new_node = dll_Node(data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            node.prev = new_node

        self.head = new_node
        # Set prev of next node to the new node

        return

    def dll_find(self, item):
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

    def dll_delete(self, item):
        '''Find a specific item in the linked list, and delete the Node and return None if not found'''
        item = self.head
        if self.head is None or item is None:
            return

        # If node to be deleted is head node
        if self.head == item:
            self.head = item.next

        # If its not the last node
        if item.next is not None:
            item.next.prev = item.prev

        # If its not the first None node
        if item.prev is not None:
            item.prev.next = item.next
