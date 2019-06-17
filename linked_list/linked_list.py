from node_spec.node import Node

class LL(object):
    """
        Linked List template
    """

    def __init__(self, head=None):
        self.head = head

    def insertion(self, data):
        """Inserts data to linked list

        :param data: data to be inserted
        :type data: int/float/str/object
        """

        node = Node(data)
        node.set_next_node(self.head)
        self.head = node

    def traversal(self):
        """
            Travels throughout the linked list
        """

        current = self.head
        while current:
            print(current.get_data())
            curent = current.get_next_node()

    def get_length(self):
        """Returns the node count of the linked list

        :return: length
        :rtype: int
        """

        length = 0
        current = self.head
        while current:
            print(current.get_data())
            curent = current.get_next_node()
            length += 1

        return length

    def search(self, data_item):
        """To search for a data item

        :param data_item: data to be searched
        :type data_item: int/float/str/object
        :return: matched node // string message
        :rtype: Node object
        """

        found = False
        current = self.head
        while current and found:
            if current.get_data() == data_item:
                found = True
            else:
                curent = current.get_next_node()

        if current is None:
            return 'element cannot be found!!'
        return current

    def deletion(self, data):
        """To delete a data item

        :param data: data to be deleted
        :type data: int/float/str/object
        """

        found = True
        current = self.head
        previous = None
        while current and found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next_node()

        if current is None:
            return 'item not in list!!'
        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next_node(current.get_next_node())
        print('item deleted!!')