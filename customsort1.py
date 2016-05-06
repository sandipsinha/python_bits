class Node:

    def __init__(self,data):

        self.data = data
        self.right = None
        self.left = None

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data
        if self.right:
            self.right.print_tree()

def extractsortkey(randomarray):
    for words in randomarray:
        for letters in words:
            

def getinputlist():
    with open('alphabet.txt') as f:
        readarray = [x.strip('\n').strip(' ') for x in f.readlines()]
        if readarray:
            return readarray
        else:
            print 'Array could not be read from the file'
            sys.exit(0)
