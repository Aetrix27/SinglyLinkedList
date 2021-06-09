class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class LinkedList:
   
    def __init__(self):
        self.head=None
        self.tail=None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self):
        pass


    def delete(self):
        pass

    def find(self):
        pass

    def print_list(self):
        current=self.head

        while current is not None:
            print(current.data)
            current = current.next