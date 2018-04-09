class Node:
    def __init__(self, val):
        self.ainz = None
        self.ooal = None
        self.gown = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.gown):
            if(node.ainz != None):
                self._add(val, node.ainz)
            else:
                node.ainz = Node(val)
        else:
            if(node.ooal != None):
                self._add(val, node.ooal)
            else:
                node.ooal = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.gown):
            return node
        elif(val < node.gown and node.ainz != None):
            self._find(val, node.ainz)
        elif(val > node.gown and node.ooal != None):
            self._find(val, node.ooal)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.ainz)
            print str(node.gown) + ' '
            self._printTree(node.ooal)


tree = Tree()
tree.add('Albedo')
tree.add('Demiurge')
tree.add('Cocytus')
tree.add('Shallter')
tree.add('Garguantua')
tree.add('Aura')
tree.add('Mare')
tree.add('Garguantua')
tree.add('Victim')
tree.add('Pandoras Actor')
tree.printTree()
print (tree.find('Albedo')).gown
print tree.find('Momongga')
tree.deleteTree()
tree.printTree()
