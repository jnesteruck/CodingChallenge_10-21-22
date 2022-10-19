'''
Weekly Coding Challenge(s)
    
1)  Given two singly linked lists that intersect at some point, find the intersecting node. Assume the lists are non-cyclical.

    For example, given A = 3 ➔ 7 ➔ 8 ➔ 10 and B = 99 ➔ 1 ➔ 8 ➔ 10, return the node with value 8. In this example, assume nodes with the same value are the exact same node objects.

    Do this in 0( m + n) time (where m and n are the lengths of the lists) and constant space.

2)  Implement a stack that has the following methods:
    • push ( val ) : push val onto the stack
    • pop: pop off and return the topmost element of the stack. If there are no elements in the stack, throw an error.
    • max: return the maximum value in the stack currently. If there are no elements in the stack, throw an error.

Each method should run in constant time.

'''
from LinkedList import LinkedList

def intersection(ll1: LinkedList, ll2: LinkedList):
    '''
    intersection

    Determines if two linked lists intersect or not. If they intersect,
    returns the intersecting node. If not, returns None.

    '''
    diff = abs(len(ll1) - len(ll2))

    k = ll1.head
    j = ll2.head
    if len(ll1) > len(ll2):
        for i in range(diff):
            k = k.next
    else:
        for i in range(diff):
            j = j.next
    while k is not None and j is not None:
        if k.value == j.value and k.next.value == j.next.value:
            return k
        k = k.next
        j = j.next

    return None

### !!! STACK CLASS IN LinkedList.py FILE !!! ###