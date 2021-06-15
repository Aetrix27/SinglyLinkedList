from LinkedList import LinkedList, DoublyLinkedList

my_ll = LinkedList()
my_ll.append(10)

my_ll.append(20)
my_ll.prepend(19)
print(my_ll.delete(21))
print(my_ll.find(10))
my_ll.print_list()

print("Doubly Linked")
my_dll = DoublyLinkedList()
my_dll.dll_append(5)
my_dll.dll_append(7)
my_dll.dll_print()
