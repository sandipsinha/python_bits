class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


    def insertLeft(self,left):
        self.left = BinaryNode(left)
        return self.left

    
    def insertRight(self,right):
        self.right = BinaryNode(right)
        return self.right


    def largest_tree_node(root_node):
        if root_node.right is not None:
            largest_tree_node(root_node.right)
        return root_node.value

    def find_second_largest_value(root_node):
        if root_node is None:
            return None

        if root_node.left and not root_node.right:
            largest_tree_node(root_node.left)

        if root_node.right and not root_node.right.left \
           and not root_node.right.right:
            return root_node.value

        return largest_tree_node(root_node.right)
            
        
    
        
    
