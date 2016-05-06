

class Node(object):
    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_code = new_next

    def print_list(self):
        current_node=self.get_next()
        while current_node:
            print current_node
            current_node = self.get_next()
        print

    def print_backward(self):
        if self.get_next() != None: 
            tail=self.get_next()
            tail.print_backward()
        print self

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

def print_list(node):
    while node:
        print node
        node = node.get_next()
    print



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next_node = node2
node2.next_node = node3
print_list(node1)
node1.print_backward()
    
        
    
