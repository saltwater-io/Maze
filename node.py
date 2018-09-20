from anytree import NodeMixin

class Node(NodeMixin):
    position = ''
    value = ''
    path = []

    def __init__(self, pos, val, path, parent=None):
        super(Node, self).__init__()
        self.position = pos
        self.value = val
        self.path = path
        self.parent = parent