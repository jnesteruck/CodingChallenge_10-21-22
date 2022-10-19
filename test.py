from LinkedList import LinkedList, Stack, EmptyLinkedListException
from challenge import *

lst1 = LinkedList([3, 7, 8, 10])
lst2 = LinkedList([99, 1, 8, 10])
lst3 = LinkedList([20, 15, 49, 1, 8, 10])

print("\nlst1: ", lst1)
print("lst2: ", lst2)
print("lst3: ", lst3)
''' OUTPUT:
lst1:  3 -> 7 -> 8 -> 10
lst2:  99 -> 1 -> 8 -> 10
lst3:  20 -> 15 -> 49 -> 1 -> 8 -> 10
'''

print("\nWhere do lst1 and lst2 intersect? ", intersection(lst1, lst2))
print("Where do lst1 and lst3 intersect? ", intersection(lst1, lst3))
print("Where do lst2 and lst3 intersect? ", intersection(lst2, lst3))
''' OUTPUT:
Where do lst1 and lst2 intersect?  8
Where do lst1 and lst3 intersect?  8
Where do lst2 and lst3 intersect?  1
'''

# CREATE A STACK
lst4 = Stack([10, 20, 30, 40, 50, 60, 70, 80])

print("lst4: ", lst4)
''' OUTPUT:
lst4:  80 -> 70 -> 60 -> 50 -> 40 -> 30 -> 20 -> 10
'''
print("Remove top of stack from lst4: ", lst4.pop())
print(lst4)
''' OUTPUT:
Remove top of stack from lst4:  80
70 -> 60 -> 50 -> 40 -> 30 -> 20 -> 10
'''

print(f"Add element ({lst4.push(90)}) to lst4: ", lst4)
print(f"Add element ({lst4.push(45)}) to lst4: ", lst4)
print(f"Add element ({lst4.push(26)}) to lst4: ", lst4)
print("Maximum value of lst4: ", lst4.max(), "\n")
''' OUTPUT:
Add element (90) to lst4:  90 -> 70 -> 60 -> 50 -> 40 -> 30 -> 20 -> 10
Add element (45) to lst4:  45 -> 90 -> 70 -> 60 -> 50 -> 40 -> 30 -> 20 -> 10
Add element (26) to lst4:  26 -> 45 -> 90 -> 70 -> 60 -> 50 -> 40 -> 30 -> 20 -> 10
Maximum value of lst4:  90
'''

## EMPTY STACK
lst5 = Stack()
print("lst5: ", lst5)
''' OUTPUT:
lst5:
'''
try:
    print("Top of stack in lst5: ", lst5.pop())
except EmptyLinkedListException as elle:
    print("Could not pop from lst5 due to the following error:")
    print(elle.message)
''' OUTPUT:
Could not pop from lst5 due to the following error:

Empty LinkedList. Could not perform action.
Try again with non-empty LinkedList.
'''

try:
    print("Maximum value in lst5: ", lst5.max())
except EmptyLinkedListException as elle:
    print("Could not find the maximum value of lst5 due to the following error:")
    print(elle.message)
''' OUTPUT:
Could not find the maximum value of lst5 due to the following error:

Empty LinkedList. Could not perform action.
Try again with non-empty LinkedList.
'''