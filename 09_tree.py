class bst:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchile = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        elif self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = bst(data)

root = bst(None)
root.insert(10)

print(root.key)

# class node:
#     def __init__(self,key):
#         self.lchild = None
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