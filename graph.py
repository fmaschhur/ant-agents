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
                    edges.append(Edge(me, down))
                    edges.append(Edge(me, right))
                elif y == maxy:               # not down
                    up = self.nodes.get((x, (y - 1)))
                    edges.append(Edge(me, up))
                    edges.append(Edge(me, right))
                else:                       # free
                    down = self.nodes.get((x, (y + 1)))
                    up = self.nodes.get((x, (y - 1)))
                    edges.append(Edge(me, down))
                    edges.append(Edge(me, right))
                    edges.append(Edge(me, up))
            elif x == maxx:                   # not right
                left = self.nodes.get(((x - 1), y))
                if y == 1 and y != maxy:      # not up
                    down = self.nodes.get((x, (y + 1)))
                    edges.append(Edge(me, down))
                    edges.append(Edge(me, left))
                elif y == maxy:               # not down
                    up = self.nodes.get((x, (y - 1)))
                    edges.append(Edge(me, up))
                    edges.append(Edge(me, left))
                else:                       # free
                    down = self.nodes.get((x, (y + 1)))
                    up = self.nodes.get((x, (y - 1)))
                    edges.append(Edge(me, down))
                    edges.append(Edge(me, left))
                    edges.append(Edge(me, up))
            else:                           # free
                right = self.nodes.get(((x + 1), y))
                left = self.nodes.get(((x - 1), y))
                if y == 1 and y != maxy:  # not up
                    down = self.nodes.get((x, (y + 1)))
                    edges.append(Edge(me, down))
                    edges.append(Edge(me, right))
                    edges.append(Edge(me, left))
                elif y == maxy:  # not down
                    up = self.nodes.get((x, (y - 1)))
                    edges.append(Edge(me, up))
                    edges.append(Edge(me, right))
                    edges.append(Edge(me, left))
                else:  # free
                    down = self.nodes.get((x, (y + 1)))
                    up = self.nodes.get((x, (y - 1)))
                    edges.append(Edge(me, down))
                    edges.append(Edge(me, right))
                    edges.append(Edge(me, up))
                    edges.append(Edge(me, left))
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
                add_me = Node(0, [], x, y)
                nodes[(x, y)] = add_me
        return nodes
