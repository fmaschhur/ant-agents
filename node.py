from math import inf
import random


class Node(object):
    def __init__(self, edges, x_pos, y_pos):  # initializes a single node and associates a list of edges to it
        self.edges = edges  # list of edges, can be empty, argument has to be 'None' for this to happen
        self.x_pos = x_pos  # x position
        self.y_pos = y_pos  # y position

    def equal(self, node):
        return self.get_x() == node.get_x() and self.get_y() == node.get_y()

    def not_equal(self, node):
        return self.get_x() != node.get_x() or self.get_y() != node.get_y()

    def get_x(self):
        return self.x_pos

    def get_y(self):  # funktion zum abfragen der y position
        return self.y_pos

    def get_x_y(self):  # funktion zum abfragen der x und y positionen
        return self.x_pos, self.y_pos

    # Alle Nachbarknoten
    def neighbours(self):
        return list(map(lambda x: x.other_node(self), self.edges))

    # Edge zu nachbarknoten
    def edge(self, node):
        for edge in self.edges:
            if edge.has_node(node):
                return edge
        return None

    # Abstand zu nachbarknoten
    def distance(self, node):
        if self.edge(node) is not None:
            return self.edge(node).distance
        return inf

    # Job id, für das Anzeigen
    def job_id(self):
        return 1
