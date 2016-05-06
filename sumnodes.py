class Node:
    def __init__(self, value, children):
        self.value=value
        self.children = children

def tree_sums(root, current_sum):
    current_sum += root.value
    if len(root.children) == 0:
        return [current_sum]
    subtree_sums = []
    for child in root.children:
        subtree_sums += tree_sums(child, current_sum)

    return subtree_sums

def depth(self):
    if not self.left and not self.right:
        return 1
    left_depth = self.left.depth() if self.left else 0
    right_depth = self.left.depth() if self.right else 0
    return max(left_depth, right_depth) + 1

tree = Node(1, [Node(2, []), Node(3, [])])
assert tree_sums(tree, 0) == [3, 4]



    

    
        
