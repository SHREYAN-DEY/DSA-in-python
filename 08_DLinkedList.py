class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None    # Initialize head as None

    def trav(self):
        if self.head is None :
            print("Linked list is empty !! ")
        else:
            currentNode = self.head
            while currentNode is not None:
                print(currentNode.data, end=" > ")
                currentNode = currentNode.next
            print("None")