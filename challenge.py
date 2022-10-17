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
from LinkedList import Node, LinkedList

def intersection(ll1: LinkedList, ll2: LinkedList):
    '''
    intersection

    Determines if two linked lists intersect or not. If they intersect,
    returns the intersecting node. If not, returns None.

    '''
    for k in ll1:
        for j in ll2:
            if k.next == None or j.next == None:
                break
            if k.next.value == j.next.value:
                return k
    return None

### !!! STACK CLASS IN LinkedList.py FILE !!! ###