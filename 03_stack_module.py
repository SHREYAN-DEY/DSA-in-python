# here we will learn how to implement stack using modules


# -------------------------
# using collection module 
# -------------------------


# import collections

# stack = collections.deque()

# def push():
#     ele = int(input("Enter a number : "))
#     stack.append(ele)
#     print(stack)

# def popElement():
#     if not stack:
#         print("Stack is empty ")
#     else:
#         print(f"Removed element is ; {stack.pop()}")
#         print(stack)

# while True:
#     print("Select the operation 1. push, 2. pop, 3. quit")
#     c = int(input())

#     if c == 1:
#         push()
#     elif c ==2:
#         popElement()
#     elif c== 3:
#          break
#     else:
#          print("Enter correct option ")



# -------------------------
# using queue module 
# -------------------------

import queue

stack = queue.LifoQueue()

def pushElement():
    ele = int(input("Enter a number : "))
    stack.put(ele)
    print(list(stack.queue))

def popElement():
    if not stack:
        print("Stack is empty ")
    else:
        print(f"Removed element is ; {stack.get()}")
        print(list(stack.queue))

while True:
    print("Select the operation 1. push, 2. pop, 3. quit")
    c = int(input())

    if c == 1:
        pushElement()
    elif c ==2:
        popElement()
    elif c== 3:
         break
    else:
         print("Enter correct option ")
