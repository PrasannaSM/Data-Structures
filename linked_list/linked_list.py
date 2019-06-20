from node_spec.node import Node

class LL(object):
    """
        Linked List template
    """

    def __init__(self, head=None):  # , tail=None):
        self.head = head
        # self.tail = tail      # for alternate way

    def insert_first(self, data):
        """Inserts data first to linked list

        :param data: data to be inserted
        :type data: int/float/str/object
        """

        node = Node(data)
        node.set_next_node(self.head)
        self.head = node

    def insert_last(self, data):
        """Inserts data last to linked list

        :param data: data to be inserted
        :type data: int/float/str/object
        """

        node = Node(data)
        node.set_next_node(None)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.get_next_node() != None:
                current = current.get_next_node()
            current.set_next_node(node)
        """
        alternate way...
        if self.head == None:
            self.head = node
        else:
            self.tail.set_next_node(node)
            self.tail = node
        """

    def traversal(self):
        """
            Travels throughout the linked list
        """

        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next_node()
        if self.head == None:
            print('empty list!!')

    def get_length(self):
        """Returns the node count of the linked list

        :return: length of list
        :rtype: int
        """

        length = 0
        current = self.head
        while current:
            current = current.get_next_node()
            length += 1

        return length

    def search(self, data):
        """To search for a data item

        :param data: data to be searched
        :type data: int/float/str/object
        :return: message
        :rtype: str
        """

        current = self.head
        while current:
            if current.get_data() == data:
                return str(data) + ' found!!'
            current = current.get_next_node()
        return str(data) + ' cannot be found!!'

    def delete(self, data):
        """To delete a data item

        :param data: data to be deleted
        :type data: int/float/str/object
        :return: message
        :rtype: str
        """

        found = False
        current = self.head
        previous = None
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next_node()

        if current is None:
            return str(data) + ' is not in list!!'
        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next_node(current.get_next_node())
        return str(data) + ' is deleted!!'