import node
import edge

class Graph(object):

    def init(self, x, y, nest):
        self.nodes = self.create_nodes(x, y)
        self.edges = self.create_edges()
        self.nest = nest
        self.antcount = 0
        return self

    def create_nodes(self, x, y):
        return

    def create_edges(self):
        return
