
class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
    
a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")


a.next = b
b.next = c
c.next = d
d.next = e

def kth_to_last_node(k,a):
    nodarray = []
    nextval = 'always'
    ami = a.next
    while ami != None:
        nodarray.append(str(ami))
        prevn = ami
        ami = ami.next
    print nodarray[len(nodarray) - k]
    return None





k = 4
print 'the last node of linked list is', kth_to_last_node(k,a)
        
        
