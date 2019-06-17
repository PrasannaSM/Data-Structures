class Node(object):
    """
        Node template class
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Returns data of current node

        :return: node data
        :rtype: int/float/str/object
        """

        return self.data

    def get_next_node(self):
        """Returns next node

        :return: next node to point
        :rtype: node object
        """

        return self.next_node

    def set_next_node(self, next_node):
        """
            Sets new next node (next_node updation)
        """

        self.next_node = next_node