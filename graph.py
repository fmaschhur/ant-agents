from node import Node
from edge import Edge
import random


class Graph(object):

    def get_node(self, x, y):
        return self.nodes.get((x, y))

    def params(self, param):
        file_obj = open(self.file)
        for line in file_obj:
            name = line.partition(': ')[0]
            if name == param:
                file_obj.close()
                return int(line.split(': ')[1])
        file_obj.close()

    def __init__(self, params_file):
        self.file = params_file
        self.x = self.params('size_x')
        self.y = self.params('size_y')
        self.nodes = self.create_nodes(self.x, self.y)
        self.edges = self.create_edges(self.x, self.y) # , self.params('thickness'))
        self.add_food(self.params('amount'), self.params('propability'))
        self.nest = self.choose_nest(self.x, self.y, self.nodes)
        self.antcount = 0 #würde das glaube ich nicht hier mit rein packen

    # verringert auf allen kanten die pheromonstärke nach den parametern
    def evaporate(self, evaporation, evap_type=1):
        for edge in self.edges:
            edge.evaporate(evaporation, evap_type)

    def add_food(self, amount, propability):
        for (x, y) in self.nodes:
            self.nodes.get((x, y)).add_food(amount, propability)

    #thickness ist ein wert zwischen 1 und 100, gibt wie wahrscheinlich eine verbindung ist
    def create_edges_new(self, maxx, maxy, thickness): #Habe das umkopiert... müsste von der Funktion her das gleiche sein
        edges = []
        for (x, y) in self.nodes:
            me = self.nodes.get((x, y))
            if x < maxx and random.randint(0, 100) < thickness:
                right = self.nodes.get(((x + 1), y))
                e = Edge(me, right)
                right.edges.append(e)
                me.edges.append(e)
                edges.append(e)
            if x > 0 and random.randint(0, 100) < thickness:
                left = self.nodes.get(((x - 1), y))
                e = Edge(me, left)
                left.edges.append(e)
                me.edges.append(e)
                edges.append(e)
            if y > 1 and random.randint(0, 100) < thickness:
                down = self.nodes.get((x, (y + 1)))
                e = Edge(me, down)
                down.edges.append(e)
                me.edges.append(e)
                edges.append(e)
            if y < maxy and random.randint(0, 100) < thickness:
                up = self.nodes.get((x, (y - 1)))
                e = Edge(me, up)
                up.edges.append(e)
                me.edges.append(e)
                edges.append(e)
        return edges

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

    def choose_nest(self, x, y, nodes):
        a = random.randint(1, x)
        b = random.randint(1, y)
        self.get_node(a, b).nest = 1
        return nodes[(a, b)]

    @staticmethod
    def create_nodes(x, y):
        nodes = {}
        for x in range(1, x+1):
            for y in range(1, y+1):
                add_me = Node(0, [])
                nodes[(x, y)] = add_me
        return nodes
