class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({})'.format(self.data)




def serialize_bt(bt):
    components = []

    def incorporate(bt, components):
        components.append(str(bt.data))
        if bt.left:
           components.append('L')
           incorporate(bt.left,components)
        if bt.right:
           components.append('R')
           incorporate(bt.right,components)
        components.append('U')
        return ''.join(components)
    incorporate(bt, components)
    components.pop()
    return ''.join(components)

BT = Node(1)
BT.left = Node(3)
BT.left.left = Node(6)
BT.right = Node(4)
BT.right.left = Node(7)
BT.right.right = Node(8)
print serialize_bt(BT)
    
           
