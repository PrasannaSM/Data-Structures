class Node(object):
    """
        Node template class
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        """Returns data of current node

        Returns:
            [object] -- node data
        """
        return self.data

    def get_next_node(self):
        """Returns next node

        Returns:
            [node object] -- next node to point
        """
        return self.next_node

    def set_next_node(self, next_node):
        """
            Sets new next node (next_node updation)
        """
        self.next_node = next_node