'''
LinkedList classes based on Tutorial provided by Giorgos Myrianthous:
https://towardsdatascience.com/python-linked-lists-c3622205da81

'''

class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    # INHERENT METHODS
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.addMultipleNodes(values)

    def __str__(self):
        return " -> ".join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    # PROPERTIES
    @property
    def values(self):
        return [node.value for node in self]
    
    # FUNCTIONS
    def addNode(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def addMultipleNodes(self, values):
        for value in values:
            self.addNode(value)
    
    def addNodeAsHead(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

### !!! STACK CLASS FOR CHALLENGE ASSIGNMENT !!! ###
class Stack(LinkedList):
    def push(self, val):
        node = Node(val, self.head)
        self.head = node
    
    def pop(self) -> Node:
        if self.tail is None:
            raise Exception
        pop_node = self.head
        self.head = pop_node.next
        return pop_node
    
    def max(self):
        if self.tail is None:
            raise Exception
        max_value = self.head.value
        for node in self:
            if node.value > max_value:
                max_value = node.value
### !!! STACK CLASS FOR CHALLENGE ASSIGNMENT !!! ###

class DoublyLinkedList (LinkedList):
    def addNode(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self
    
    def addNodeAsHead(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            current_head = self.head
            self.head = Node(value, current_head)
            current_head.prev = self.head
        return self.head