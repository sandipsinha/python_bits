class Node:
    def __init__(self, val):
        self.v = val
        self.l = None
        self.r = None

class Tree:
    def __init__(self):
        self.root = None

    def getroot(self):
        return self.root

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l != None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        elif val > node.v:
            if node.r != None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root == None:
            return None
        else:
            self_find(self, val, self.root)

    def _find(self, val, node):
        if val == node.v:
            return node
        elif val < node.v:
            if node.l != None:
                self._find(val, node.l)
        elif val > node.v:
            if node.r != None:
                self._find(val, node.r)
                
    def __str__(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node != None:
            print _printTree(node.l)
            print str(node.v) + ' '
            print _printTree(node.r)
            
        
                
            
                
            
