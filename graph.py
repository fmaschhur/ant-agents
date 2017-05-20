from node import Node
from edge import Edge
import random


class Graph(object):
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
        self.x_size = self.params('size_x')
        self.y_size = self.params('size_y')
        self.nodes = self.create_nodes()
        self.edges = self.create_edges(self.x_size, self.y_size, self.params("thickness"))
        self.nest = self.choose_nest()
        self.add_food(self.params('food_src_count'), self.params('food_amount'))

    # verringert auf allen kanten die pheromonstärke nach den parametern
    def evaporate(self, evaporation, evap_type=1):
        for edge in self.edges:
            edge.evaporate(evaporation, evap_type)

    def add_food(self, number, maxamount):
        xylist = []
        for x in range(1, (self.x_size + 1)):
            for y in range(1, (self.y_size + 1)):
                if x != self.nest.get_x() and y != self.nest.get_y():
                    xylist.append((x, y))
        random.shuffle(xylist)
        sources = xylist[:number]
        for (x, y) in sources:
            self.nodes.get((x, y)).add_food(random.randint(1, maxamount))

    def create_edges(self, max_x, max_y, thickness):
        edges = []
        for (x, y) in self.nodes:
            me = self.nodes.get((x, y))
            if x < max_x and random.randint(0, 100) <= thickness:
                right = self.nodes.get(((x + 1), y))
                edges.append(Edge(me, right))
            if y < max_y and random.randint(0, 100) <= thickness:
                down = self.nodes.get((x, (y + 1)))
                edges.append(Edge(me, down))
        return edges

    def create_labyrinth_edges(self):
        edges = []
        currnode = self.nodes[0]
        lastnode = self.nodes[-1]
        while currnode != lastnode:
            nextnode = self.get_labyrinth_neighbour(currnode.get_x(), currnode.get_y())
            edges.append(Edge(currnode, nextnode))
            currnode = nextnode
        return edges

    def get_labyrinth_neighbour(self, x, y):
        nodes = []
        if (x + 1, y) in self.nodes:
            nodes.append(self.nodes[(x + 1, y)])
        if (x, y + 1) in self.nodes:
            nodes.append(self.nodes[(x, y + 1)])
        return random.choice(nodes)

    def choose_nest(self):
        a = random.randint(1, self.x_size)
        b = random.randint(1, self.y_size)
        self.nodes[(a, b)].nest = True
        return self.nodes[(a, b)]

    # def get_node(self, x, y):
    #     return self.nodes.get((x, y))

    def create_nodes(self):
        nodes = {}
        for x in range(1, self.x_size + 1):
            for y in range(1, self.y_size + 1):
                add_me = Node(0, [], x, y)
                nodes[(x, y)] = add_me
        return nodes
