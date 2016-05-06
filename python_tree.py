class Tree(object):

    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self,root):

        def serializeHelper(data):
            if not data:
                vals.append('#')
            else:
                vals.append(str(node.val))
                serialize(data.left)
                serialize(data.right)
        vals=[]
        serializeHelper(root)
        return ''.join(vals)

    def deseriailize(self, data):

        def deserializehelper():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = Tree(int(val))
                node.left = deserializehelper()
                node.right = deserializehelper()
                return node
        def isplit(source, sep):
            sepsize = len(sep)
            start = 0
            while True:
                idx = source.find(sep, start)
                if idx == -1:
                    yield source[start:]
                yield source[start:idx]
                start = idx + sepsize
        vals = iter(split(data, ' '))
        return deserializehelpder()
                    

                    
                
            
        
            
            
        
