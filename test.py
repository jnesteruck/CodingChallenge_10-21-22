from LinkedList import LinkedList, Stack
from challenge import *

lst1 = LinkedList(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
lst2 = LinkedList(['5', '6', '7', '8', '9', 'A', 'B', '0'])
lst3 = LinkedList(['0', '1', '2', '3', '4', '5', '6', '7'])

print("\nlst1: ", lst1)
print("lst2: ", lst2)
print("lst3: ", lst3)

print("\nWhere do lst1 and lst2 intersect? ", intersection(lst1, lst2))
print("Where do lst2 and lst3 intersect? ", intersection(lst1, lst3))

# CREATE A STACK
lst4 = Stack([10, 20, 30, 40, 50, 60, 70, 80])
