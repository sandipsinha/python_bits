class binarynode(object):
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def search(self, value):
        if self.value == value:
            return True
        else:
            if self.value > value:
                if self.left != None:
                    self.left.search(value)
                else:
                    return False
            else:
                if self.right!= None:
                    self.right.search(value)
                else:
                    return False
    def insert(self, item):
        if self.value == item:
            return
        else:
            if self.value > item:
                if self.left != None:
                    self.left.insert(item)
                else:
                    self.left = binarynode(item)
            else:        
                if self.right != None:
                    self.right.insert(item)
                else:
                    self.right = binarynode(item)
