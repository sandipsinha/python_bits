class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value < data:
            if self.rightChild is not None:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
        elif self.value > data:
            if self.leftChild is not None:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)

    def traverse(self, data):
        if self.data == data:
            if self.leftChild is not None:
                self.leftChild.traverse(self.leftChild)
            if self.rightChild is not None:
                self.rightChild.traverse(self.rightChild)
            
