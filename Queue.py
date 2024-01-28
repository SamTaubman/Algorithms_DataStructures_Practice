#Implementing a Queue with a list, O(n) time for pop and append -> amortized O(1) time for append
queue = []
queue.append()
queue.pop(0)

#Implementing a Queue with collections.deque
import collections

queue = collections.deque()
queue.append()
queue.popleft()

#Implementing a Queue with a Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None
    
    def enqueue(self, item):
        temp = Node(item)

        if self.tail is None:
            self.head = self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp

    def dequeue(self):
        if self.isEmpty():
            return
        
        temp = self.head
        self.head = temp.next
 
        if self.head is None:
            self.tail = None

    