from LinkedList import LinkedList, Stack, EmptyLinkedListException
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

print("lst4: ", lst4)
print("Remove top of stack from lst4: ", lst4.pop())
print(lst4)

print(f"Add element ({lst4.push(90)}) to lst4: ", lst4)
print(f"Add element ({lst4.push(45)}) to lst4: ", lst4)
print(f"Add element ({lst4.push(26)}) to lst4: ", lst4)
print("Maximum value of lst4: ", lst4.max())
print()

## EMPTY STACK
lst5 = Stack()
print("lst5: ", lst5)
try:
    print("Top of stack in lst5: ", lst5.pop())
except EmptyLinkedListException as elle:
    print("Could not pop from lst5 due to the following error:")
    print(elle.message)

try:
    print("Maximum value in lst5: ", lst5.max())
except EmptyLinkedListException as elle:
    print("Could not find the maximum value of lst5 due to the following error:")
    print(elle.message)