
# first module using deque in collection module

# import collections

# q = collections.deque()

#            -------------
# enqueue -->    queue    -->dequeue
#            -------------

# q.appendleft(10)
# q.appendleft(20)
# q.appendleft(30)

# print(q)

# q.pop()
# print(q)


#            -------------
# dequeue <--    queue    <--enqueue
#            -------------

# q.append(10)
# q.append(20)
# q.append(30)

# print(q)

# q.popleft()
# print(q)




# second module using queue in collection module

import queue

q = queue.Queue(3)

q.put(10,timeout=1)
q.put(20,timeout=1)
q.put(30,timeout=1)

print(list(q.queue))

q.put(40,timeout=1) 