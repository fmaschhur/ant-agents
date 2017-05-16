import node
import edge
import random


class Graph(object):

    def __init__(self, x, y):
        self.nodes = self.create_nodes(x, y)
        self.edges = self.create_edges()
        self.nest = self.choose_nest(x, y, self.nodes)
        self.antcount = 0

    def create_nodes(self, x, y):
        nodes = {}
        for x in range(0, x+1):
            for y in range(0, y+1):
                add_me = node.__init__(0, None)
                nodes[(x, y)] = add_me
        return nodes

    def create_edges(self):
        edges = []
        for (x, y) in self.nodes:
            if x == 1:          # not left
                if y == 1:      # not up
                    edges.append(edge.init(self.nodes(x, y), self.nodes(x, (y + 1))))
                    edges.append(edge.init(self.nodes(x, y), self.nodes((x + 1), y)))

    def choose_nest(self, x, y, nodes):
        a = random.randint(0, x)
        b = random.randint(0, y)
        return nodes[(a, b)]
