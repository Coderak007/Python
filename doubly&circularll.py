                              # Doubly linked list implementation in Python

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        t1 = self.head
        while t1.next != None:
            t1 = t1.next

        t1.next = temp
        temp.prev = t1

    def insertAtStart(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp    

    def printDLL(self):
        t1 = self.head
        while t1 != None:
            print(t1.value , end = " <--> ")
            t1 = t1.next
        

obj = DoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtStart(5)
obj.printDLL()

