# class bst:
#     def __init__(self,key = None):
#         self.key = key
#         self.left = None
#         self.right = None

#     def insert(self, data):
#         if self.key is None:
#             self.key = data
#             return
#         if self.key > data:
#             if self.left:
#                 self.left.insert(data)
#             else:
#                 self.left = bst(data)
#         else:
#             if self.right:
#                 self.right.insert(data)
#             else:
#                 self.right = bst(data)

# root = bst()
# root.insert(10)

# print(root.key)

class node:
    def __init__(self,value = None):
        self.left = None
        self.value = value
        self.right = None

class bst:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value,self.root)

    def _insert(self, value, currNode):
        if value < currNode.value:
            if currNode.left is None:
                currNode.left = node(value)
            else:
                self._insert(value,currNode.left)
        elif value > currNode.value:
            if currNode.right is None:
                currNode.right = node(value)
            else:
                self._insert(value,currNode.right)
        else:
            print("value already in tree")


    def printTree(self): 
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, currNode):
        if currNode is not None:
            self._printTree(currNode.left)
            print(str(currNode.value))
            self._printTree(currNode.right)




tree = bst()
tree.insert(10)
tree.insert(10)
tree.insert(9)
tree.insert(11)

tree.printTree()