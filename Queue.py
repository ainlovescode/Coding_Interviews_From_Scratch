# DATA STRUCTURES CHEATSHEET
# Compiled by @ainlovescode
# Find me on GitHub, LinkedIn, Facebook and Instagram!

class Queue:
    def __init__(self, queue):
        self.queue = queue

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

myQueue = Queue([1,2,3,4])

myQueue.enqueue(0)
print(myQueue.queue)

print(myQueue.dequeue())
print(myQueue.queue)
