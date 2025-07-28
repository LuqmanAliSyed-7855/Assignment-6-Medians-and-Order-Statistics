"""Elaborating two classes named Stack and Queue and implement the operation of each of them.
The stack class implements methods to push, pop, peek the stack, empty stack check and print the stack. 
Queue provides enqueueing, dequeueing, peeking, checking empty status, and printing the queue. 
In the example usage, both data structures are used by adding, removing, and accessing elements 
to illustrate their behavior. Both classes have an efficient data handling approach by the use 
of list-based implementation in Python.
"""

# Stack implementation

class Stack:
    def __init__(self):
        # Initializing an empty stack
        self.stack = []

    def push(self, value):
        # Pushing a value onto the stack
        self.stack.append(value)

    def pop(self):
        # Popping the top value from the stack
        if not self.is_empty():
            return self.stack.pop()  
        else:
            return None  

    def peek(self):
        # Peeking the top value of the stack
        if not self.is_empty():
            return self.stack[-1]  
        else:
            return None 

    def is_empty(self):
        # Checking if the stack is empty
        return len(self.stack) == 0

    def display(self):
        # Displaying the current stack
        return self.stack


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  
print(stack.peek())  
print(stack.display())  


# Queue implementation

class Queue:
    def __init__(self):
        # Initializing an empty queue
        self.queue = []

    def enqueue(self, value):
        # Enqueuing a value into the queue
        self.queue.append(value)

    def dequeue(self):
        # Dequeuing a value from the queue
        if not self.is_empty():
            return self.queue.pop(0)  
        else:
            return None 
        
    def peek(self):
        # Peeking the front value of the queue
        if not self.is_empty():
            return self.queue[0]  
        else:
            return None  

    def is_empty(self):
        # Checking if the queue is empty
        return len(self.queue) == 0

    def display(self):
        # Displaying the current queue
        return self.queue


# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.dequeue()) 
print(queue.peek())  
print(queue.display())  

