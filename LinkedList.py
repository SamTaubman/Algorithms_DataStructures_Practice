class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to add a node at begin of LL
    def insertAtBegin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, value, index):
        new_node = Node(value)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(value)
        else:
            while(current_node is not None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
 
    # Method to add a node at the end of LL
 
    def insertAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node
 
    # Update node of a linked list
        # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.value = val
        else:
            while(current_node is not None and position != index):
                position = position+1
                current_node = current_node.next
 
            if current_node is not None:
                current_node.value = val
            else:
                print("Index not present")
 
    # Method to remove first node of linked list
 
    def remove_first_node(self):
        if(self.head is None):
            return
 
        self.head = self.head.next
 
    # Method to remove last node of linked list
    def remove_last_node(self):
 
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None
 
    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head is None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node is not None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node is not None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
 
    # Method to remove a node from linked list
    def remove_node(self, value):
        current_node = self.head
 
        while(current_node is not None and current_node.next.value != value):
            current_node = current_node.next
 
        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next
 
    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
 
    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.value)
            current_node = current_node.next
 
 
# create a new linked list
llist = LinkedList()

#Doubly Linked List in Python
# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.head = None
    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("The list is empty")
    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None
    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
    # Traversing and Displaying each element of the list
    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            n = self.head
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")