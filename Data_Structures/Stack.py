class Stack:
    def __init__(self):
        self.stack = []

    def pushIntoStack(self, item):
        self.stack.insert(0, item)

    def popFromStack(self):
        return self.stack.pop(0)

    def printStack(self):
        print(self.stack)

myStack = Stack()

myStack.pushIntoStack(5)
myStack.pushIntoStack(4)
myStack.pushIntoStack(3)
myStack.pushIntoStack(2)
myStack.pushIntoStack(1)

myStack.printStack()

print(myStack.popFromStack())
myStack.printStack()

