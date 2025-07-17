# class bst:
#     def __init__(self,value = None):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, data):
#         if self.value is None:
#             self.value = data
#             return
#         if self.value > data:
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

# print(root.value)

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
            print(currNode.value," ", end="")
            self._printTree(currNode.right)

    # def printTree(self, root):
    #     if root is not None:
    #         self.printTree(root.left)
    #         print(root.value," ", end="")
    #         self.printTree(root.right)




tree = bst()
tree.insert(10)
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.insert(6)
tree.insert(18)

tree.printTree()
# tree.printTree(tree.root) # this is for the second type of print function