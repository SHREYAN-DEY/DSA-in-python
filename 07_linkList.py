class node:
    def __init__(self,data):
        self.data = data    # Assign data
        self.next = None     # Initialize next as None

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

    def addStart(self,data):
        newNode = node(data)        # create the new node

        newNode.next = self.head    # assign the new node to the head
        self.head = newNode         # update the head 

    def addEnd(self,data):
        newNode = node(data)        # create a new node

        if self.head is None:       # if the linked list is empty
            self.head = newNode
        else:                       # if the linked list is not empty
            n = self.head
            while n.next is not None:
                n = n.next          # iterate to the last node

            n.next = newNode        # assign the last node 

    def addIndex(self,data,index):
        newNode = node(data)

        if self.head is None:
            print("The linked list is empty")
            self.head = newNode
            return
        else:
            p = None
            n = self.head
            i = 0
            while i < index - 1:
                p = n
                n = n.next
                i += 1

            p.next = newNode
            newNode.next = n

    def rmvStart(self):
        n = self.head
        n = n.next
        self.head = n

    def rmvEnd(self):
        if self.head is None:
            print("The linked list is empty ")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None


        


ll1 = linkedList()

ll1.addStart(10)
ll1.addStart(20)
ll1.addStart(30)
ll1.addEnd(900)

ll1.trav()
ll1.addIndex(69,3)

# ll1.rmvStart()
ll1.rmvEnd()
ll1.trav()