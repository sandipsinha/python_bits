class MyLinkedList(LinkedList):

    def __add_reverse__(self, first_node, second_node, carry):
        if type(carry) != int and carry < 0:
            raise ValueError('Invalid int argument: carry')

        # Base case
        if first_node is None and second_node is None and carry == 0:
            return None

        # Recursive case
        value = carry
        value += first_node.data if first_node is not None else 0
        value += second_node.data if second_node is not None else 0
        new_carry = 1 if value >= 10 else 0
        remainder = value % 10
        node = Node(remainder)
        node.next = self.__add_reverse__(
            first_node.next if first_node is not None else None,
            second_node.next if first_node is not None else None,
            new_carry)
        return node

    def add_reverse(self, first_list, second_list):
        if first_list is None or second_list is None:
            return None
        head = self.__add_reverse__(first_list.head, second_list.head, 0)
        return MyLinkedList(head)


