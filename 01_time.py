# here we will measure time of execution of a program 

import time 

start = time.time()


# for i in range (1,101):
#     print(i)

i = 1
while i < 101:
    print(i)
    i += 1

print(time.time() - start)

# btw this is not a good way to measure time efficiency