from singly_linked_list import SinglyLinkedList
from node import Node

my_list = SinglyLinkedList()

# append 10
node_a = Node(10)
my_list.append(node_a)

# append 15
node_b = Node(15)
my_list.append(node_b)

# prepend 25
node_c = Node(25)
my_list.prepend(node_c)

# insert 7 after 25
node_d = Node(7)
my_list.insert_after(node_c, node_d)

# error checking when node doestn exist
node_e = Node(9)
node_g = Node(3)
my_list.insert_after(node_e, node_g)

print(f"My linked list: {my_list.head.data}, {my_list.head.next.data}, {my_list.head.next.next.data}, {my_list.tail.data}")

