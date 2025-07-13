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
        if self.head is None:
            newNode = node(data)
            self.head = newNode
        else:
            newNode = node(data)
            newNode.next = self.head
            self.head = newNode







dll1 = DLL()

dll1.addStart(10)
dll1.addStart(20)
dll1.addStart(30)
dll1.addStart(40)

dll1.trav()