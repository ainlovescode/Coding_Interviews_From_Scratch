# DATA STRUCTURES CHEATSHEET - LINKEDLIST
# Compiled by @ainlovescode
# Find me on GitHub, LinkedIn, Facebook and Instagram!

class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        self.next = value

class LinkedList:
    def __init__(self):
        self.head = None

    def getLinkedList(self):
        temp = self.head
        while temp:
            print(temp.value, sep = " -> ")
            temp = temp.next()
        print(temp.value, sep = "")


myLinkedList = LinkedList()
myHeadNode = LinkedNode(0)
myLinkedList.head = myHeadNode
node_1 = LinkedNode(1)
node_2 = LinkedNode(2)

myHeadNode.next = node_1
node_1.next = node_2

myLinkedList.getLinkedList()
