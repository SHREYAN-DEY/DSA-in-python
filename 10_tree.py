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
            print("\n")

    def _printTree(self, currNode):
        if currNode is not None:
            self._printTree(currNode.left)
            print(currNode.value," ", end="")
            self._printTree(currNode.right)


    def search(self, value, root):
        if root is None:
            print(f"{value} is NOT present in the tree")
            return False
        
        if root.value == value:
            print(f"{value} is present in the tree")
            return True
        elif value < root.value:
            self.search(value, root.left)
        else:
            self.search(value, root.right)

    # def delete(self,value):
    #     if self.value is None:
    #        print("Tree is empty !!")
    #        return
    #     if value < self.value:
    #         if self.left:
    #             self.left = self.left.delete(value)
    #         else:
    #             print("Given node is not present ")
    #     elif value > self.value:
    #         if self.right:
    #             self.right = self.right.delete(value)
    #         else:
    #             print("Given node is not present ")
    #     else:
    #         if self.left is None:
    #             temp = self.right
    #             self = None
    #             return temp
    #         if self.right is None:
    #             temp = self.left
    #             self = None
    #             return temp
    #         node = self.right
    #         while node.left:
    #             node = node.left
    #         self.value = node.value
    #         self.right = self.right.delete(node.value)

    def delete(self, value):
        if self.root is None:
            print("Tree is empty")
            return
        self.root = self._delete(self.root,value)

    def _delete(self,currNode, value):
        if currNode is None:
            print("Given node is not present ")
            return None
        if value < currNode.value:
            currNode.left = self._delete(currNode.left, value)
            return currNode
        elif value > currNode.value:
            currNode.right = self._delete(currNode.right, value)
            return currNode
        else:
            if currNode.left is None:
                temp = currNode.right
                return temp
            elif currNode.right is None:
                temp = currNode.left
                return temp
            
            successor = currNode.right
            while successor.left is not None:
                successor = successor.left

            currNode.value = successor.value

            currNode.right = self._delete(currNode.right, successor.value)
            return currNode
        
    def minNode(self):
        currNode = self.root
        if currNode is None:
            print("Tree is empty")
            return
        else:
            while currNode.left:
                currNode = currNode.left
            print(f"The min node is {currNode.value}")

    def maxNode(self):
        currNode = self.root
        if currNode is None:
            print("Tree is empty")
            return
        else:
            while currNode.right:
                currNode = currNode.right
            print(f"The max node is {currNode.value}")



            


tree = bst()
tree.insert(10)
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.insert(6)
tree.insert(18)

tree.printTree()

tree.search(20,tree.root)

# tree.delete(10)
# tree.printTree()

tree.minNode()
tree.maxNode()

