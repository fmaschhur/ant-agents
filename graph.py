from node import Node
from edge import Edge
import random


class Graph(object):

    def __init__(self, x, y):
        self.nodes = self.create_nodes(x, y)
        self.edges = self.create_edges(x, y)
        self.nest = self.choose_nest(x, y, self.nodes)
        self.antcount = 0

    def create_edges(self, maxx, maxy):
        edges = []
        for (x, y) in self.nodes:
            me = self.nodes.get((x, y))
            if x == 1 and x != maxx:          # not left
                right = self.nodes.get(((x + 1), y))
                if y == 1 and y != maxy:      # not up
                    down = self.nodes.get((x, (y + 1)))
                    e1 = Edge(me, down)
                    e2 = Edge(me, right)
                    down.edges.append(e1)
                    down.edges.append(e2)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    right.edges.append(e1)
                    right.edges.append(e2)
                    edges.append(e1)
                    edges.append(e2)
                elif y == maxy:               # not down
                    up = self.nodes.get((x, (y - 1)))
                    e1 = Edge(me, up)
                    e2 = Edge(me, right)
                    up.edges.append(e1)
                    up.edges.append(e2)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    right.edges.append(e1)
                    right.edges.append(e2)
                    edges.append(e1)
                    edges.append(e2)
                else:                       # free
                    down = self.nodes.get((x, (y + 1)))
                    up = self.nodes.get((x, (y - 1)))
                    e1 = Edge(me, down)
                    e2 = Edge(me, right)
                    e3 = Edge(me, up)
                    down.edges.append(e1)
                    down.edges.append(e2)
                    down.edges.append(e3)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    me.edges.append(e3)
                    up.edges.append(e1)
                    up.edges.append(e2)
                    up.edges.append(e3)
                    right.edges.append(e1)
                    right.edges.append(e2)
                    right.edges.append(e3)
                    edges.append(e1)
                    edges.append(e2)
                    edges.append(e3)
            elif x == maxx:                   # not right
                left = self.nodes.get(((x - 1), y))
                if y == 1 and y != maxy:      # not up
                    down = self.nodes.get((x, (y + 1)))
                    e1 = Edge(me, down)
                    e2 = Edge(me, left)
                    down.edges.append(e1)
                    down.edges.append(e2)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    left.edges.append(e1)
                    left.edges.append(e2)
                    edges.append(e1)
                    edges.append(e2)
                elif y == maxy:               # not down
                    up = self.nodes.get((x, (y - 1)))
                    e1 = Edge(me, up)
                    e2 = Edge(me, left)
                    up.edges.append(e1)
                    up.edges.append(e2)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    left.edges.append(e1)
                    left.edges.append(e2)
                    edges.append(e1)
                    edges.append(e2)
                else:                       # free
                    down = self.nodes.get((x, (y + 1)))
                    up = self.nodes.get((x, (y - 1)))
                    e1 = Edge(me, down)
                    e2 = Edge(me, left)
                    e3 = Edge(me, up)
                    down.edges.append(e1)
                    down.edges.append(e2)
                    down.edges.append(e3)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    me.edges.append(e3)
                    up.edges.append(e1)
                    up.edges.append(e2)
                    up.edges.append(e3)
                    left.edges.append(e1)
                    left.edges.append(e2)
                    left.edges.append(e3)
                    edges.append(e1)
                    edges.append(e2)
                    edges.append(e3)
            else:                           # free
                right = self.nodes.get(((x + 1), y))
                left = self.nodes.get(((x - 1), y))
                if y == 1 and y != maxy:  # not up
                    down = self.nodes.get((x, (y + 1)))
                    e1 = Edge(me, down)
                    e2 = Edge(me, right)
                    e3 = Edge(me, left)
                    down.edges.append(e1)
                    down.edges.append(e2)
                    down.edges.append(e3)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    me.edges.append(e3)
                    right.edges.append(e1)
                    right.edges.append(e2)
                    right.edges.append(e3)
                    edges.append(e1)
                    edges.append(e2)
                    edges.append(e3)
                elif y == maxy:  # not down
                    up = self.nodes.get((x, (y - 1)))
                    e1 = Edge(me, up)
                    e2 = Edge(me, right)
                    e3 = Edge(me, left)
                    up.edges.append(e1)
                    up.edges.append(e2)
                    up.edges.append(e3)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    me.edges.append(e3)
                    right.edges.append(e1)
                    right.edges.append(e2)
                    right.edges.append(e3)
                    edges.append(e1)
                    edges.append(e2)
                    edges.append(e3)
                else:  # free
                    down = self.nodes.get((x, (y + 1)))
                    up = self.nodes.get((x, (y - 1)))
                    e1 = Edge(me, down)
                    e2 = Edge(me, right)
                    e3 = Edge(me, up)
                    e4 = Edge(me, left)
                    down.edges.append(e1)
                    down.edges.append(e2)
                    down.edges.append(e3)
                    down.edges.append(e4)
                    me.edges.append(e1)
                    me.edges.append(e2)
                    me.edges.append(e3)
                    me.edges.append(e4)
                    up.edges.append(e1)
                    up.edges.append(e2)
                    up.edges.append(e3)
                    up.edges.append(e4)
                    right.edges.append(e1)
                    right.edges.append(e2)
                    right.edges.append(e3)
                    right.edges.append(e4)
                    edges.append(e1)
                    edges.append(e2)
                    edges.append(e3)
                    edges.append(e4)
        return edges

    @staticmethod
    def choose_nest(x, y, nodes):
        a = random.randint(0, x)
        b = random.randint(0, y)
        return nodes[(a, b)]

    @staticmethod
    def create_nodes(x, y):
        nodes = {}
        for x in range(1, x+1):
            for y in range(1, y+1):
                add_me = Node(0, [])
                nodes[(x, y)] = add_me
        return nodes
