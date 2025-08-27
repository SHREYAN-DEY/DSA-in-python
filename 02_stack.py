# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# stack.append(50)
# stack.append(60)

# print(stack)

# element = stack.pop()

# print(f"Popped element from the stack is : {element}")

# print(stack)

# print(stack[-1])




# --------------------------------
# proper example with full code 
#---------------------------------



stack = []

def push():
    element = int(input("Enter a number : "))
    stack.append(element)
    print(stack)

def popElement():
        if not stack:
            print("Stack is empty ")
        else:
            e = stack.pop()
            print(f"Removed element is : {e}")
            print(stack)


while True:
    print("Select the operation 1. push, 2. pop, 3. quit")
    c = int(input())

    if c == 1:
        push()
    elif c ==2:
        popElement()
    elif c== 3:
         break
    else:
         print("Enter correct option ")
