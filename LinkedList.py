#JOHN DAVE B. FUERTE

#Linked List with Remove Duplicate

#github.com/rameeeen23

#johndavefuerte@gmail.com

class Node:
    def __init__(self, contents, next = None):
        self.contents = contents
        self.next = next

    def getContents(self):
        return self.contents

    def setContents(self, val):
        self.contents = val

    def getNext(self):
        return self.next

    def setNext(self, val):
        self.next = val


class Linkedlist:
    def __init__(self, headnode = None):
        self.headnode = headnode
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, contents):
        newNode = Node (contents, self.headnode)
        self.headnode = newNode
        self.size +=1
        return True

    def printNode(self):
        dave = self.headnode
        while dave:
            print(dave.contents)
            dave = dave.getNext()

myList = Linkedlist()
print ("Inserting")
print (myList.addNode(2))
print (myList.addNode(4))
print (myList.addNode(6))
print (myList.addNode(8))
print (myList.addNode(10))
print (myList.addNode(12))
print (myList.addNode(14))
print (myList.addNode(16))
print (myList.addNode(18))
print (myList.addNode(20))
print ("Printing")
myList.printNode()
print ("Size")
print (myList.getSize())