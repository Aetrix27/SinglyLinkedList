from LinkedList import LinkedList

my_ll = LinkedList()
my_ll.append(10)

print(my_ll.head.data)
print(my_ll.tail.data)

my_ll.append(20)
print(my_ll.head.next.data)