# Queue --> A queue is a python data structure for storing elements that support a first-in-first-out operation (FIFO)

# We might also use a list as the container

buffer = [] # Creating an empty list called 'buffer'

buffer.insert(0,'midas') # Items are always added to the 0th position in a Queue
buffer.insert(0,'spades')
print(buffer)

print()
# But the problem with a list is its dynamic behaviour where allocation of memory when the current one is full 
# then it will have to copy all those elements into a new memory location. So using a deque from collections module is preferrable


from collections import deque   # import the deque module
myQueue = deque()   # Creating a new instance of the mdoule
myQueue.appendleft('babbs') # appendleft() is a method that adds items to the leftmost side or the 0th position just like the above insert() function
myQueue.appendleft('midas')
myQueue.appendleft(88)

print(myQueue)
myQueue.pop()   # pop() operation/function removes the rightmost item i.e the first added item
print(myQueue)

print()


# To implement a proper class of deque

class Queue:
    def __init__(self): # A constructor
        self.buffer = deque()

    def enqueue(self, val):      # Method that inserts items into the queue from the left
        self.buffer.appendleft(val) # val == 'value'

    def dequeue(self):      # Method that removes the first (right-most) element
        self.buffer.pop()
    
    def isEmpty(self):      # Method checks and returns the size of the element in a boolean expression
        return len(self.buffer) == 0

    def sizeOf(self):   # Method returns the len of the queue
        return len(self.buffer)



# Use the above created class by creating an instance / object of it

myQueue = Queue()

print(myQueue.buffer) # Printing the entire container / queue
print()

myQueue.enqueue('Shabiha')
print(myQueue.isEmpty())
print(myQueue.sizeOf())
print(myQueue.buffer)