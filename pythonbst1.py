class Treenode:
    def __init__(self,key, value, left=None,
                 right=None,parent=None):
        self.key = key
        self.payload=value
        self.leftChild = lc
        self.rightChild = lc
        self.parent = parent

    def hasleftChild(self):
        return self.leftChild
    
    def hasrightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasleftChild():
            self.leftchildparent = self
        if self.hasrightChild():
            self.leftrightparent = self
            

        
        
    
