# Practical 5: Airtel queue
from collections import deque
queue = deque([1, 2, 3, 4, 5])
print("Initial queue:", list(queue))

# Serve 2 clients (dequeue)
queue.popleft()
queue.popleft()

print("Queue after serving 2:", list(queue))
print("Front client now:", queue[0])

#At BK ATM, 7 clients queue. Who is last served?
from collections import deque

# Practical 6: BK ATM queue
queue = deque([1, 2, 3, 4, 5, 6, 7])
print("Initial queue:", list(queue))

# Last served = last element in queue
print("Last served client:", queue[-1])
