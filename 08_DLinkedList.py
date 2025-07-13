class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DLL:
    def __init__(self):
        self.head = None    # Initialize head as None

    def trav(self):
        if self.head is None :
            print("Linked list is empty !! ")
        else:
            currentNode = self.head
            print("None > ", end="")
            while currentNode is not None:
                print(currentNode.data, end=" > ")
                currentNode = currentNode.next
            print("None")

    def addStart(self, data):
        if self.head is None:           # if the linked list is empty
            newNode = node(data)
            self.head = newNode         
        else:                           # if the linked list is not empty
            newNode = node(data)
            newNode.next = self.head
            self.head = newNode

    def addEnd(self, data):
        newNode = node(data)

        if self.head is None:           # if the linked list is empty
            self.head = newNode
        else:                           # if the linked list is not empty
            n = self.head
            while n.next is not None:   # iterate to the last node
                n = n.next
            n.next = newNode            # assign the last node 







dll1 = DLL()

dll1.addStart(10)
dll1.addStart(20)
dll1.addStart(30)
dll1.addStart(40)
dll1.addEnd(999)

dll1.trav()