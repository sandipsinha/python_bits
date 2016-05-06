class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'Node({})'.format(self.val)

BT = Node(1)
BT.left = Node(3)
BT.left.left = Node(6)
BT.right = Node(4)
BT.right.left = Node(7)
BT.right.right = Node(8)

def serialize(bt):
    component = []
    def incorporate(bt, component):  
        component.append(str(bt.val))
        if bt.left:
            component.append('L')
            incorporate(bt.left, component)
        if bt.right:
            component.append('R')
            incorporate(bt.right, component)
        component.append('U')

    incorporate(bt, component)
    component.pop()
    return ''.join(component)

print 'the tree is', serialize(BT)
    
