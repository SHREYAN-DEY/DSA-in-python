class bst:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = bst(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = bst(data)

root = bst(None)
root.insert(10)

print(root.key)

# class node:
#     def __init__(self,key):
#         self.left = None
#         self.key = key
#         self.rchild = None

# class bst:
#     def __init__(self):
#         self.root = None
    
#     def addChild(self, key):
#         newNode = node(key)
#         if self.root is None:
#             self.key = newNode
#         elif 