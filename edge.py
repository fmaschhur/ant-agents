import random

class Edge(object):
    def __init__(self, node1, node2, length):  # initialises an edge given 2 (different) nodes, order doesn't matter
        self.node1 = node1  # first node
        self.node2 = node2  # second node
        self.length = length    # distance
        node1.edges.append(self)  # save edge in nodes
        node2.edges.append(self)  #

    def has_nodes(self, node1, node2):  # falls node1, node2 die Nodes der Kante sind return true
        return self.other_node(node1) == node2

    def has_node(self, node):  # falls node einer der beiden Nodes der Kante ist return true
        return (self.node1 == node or self.node2 == node)

    def connected_nodes(self):
        return (self.node1, self.node2)

    def other_node(self, node):
        if node == self.node1:
            return self.node2
        elif node == self.node2:
            return self.node1
        else:
            return None
