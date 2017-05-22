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
        # self.edges = self.create_labyrinth_edges(self.x_size, self.y_size)
        self.edges = self.create_edges(self.x_size, self.y_size, self.params("thickness"))
        if self.params('f') == 0 and self.params('e') == 0:
            if self.params('a') == 0:
                self.nest = self.choose_nest()
                self.add_food(self.params('food_src_count'), self.params('food_max'), self.params('food_min'))
            else:
                self.nodes[(2, 2)].nest = True
                self.nest = self.nodes[(2, 2)]
                self.nodes[(6, 7)].add_food(500)
                self.nodes[(5, 3)].add_food(500)
                self.nodes[(1, 6)].add_food(500)
                self.nodes[(3, 5)].add_food(500)
        if self.params('e') and not self.params('f'):
            self.create_suboptimal_path(self.x_size, self.y_size)
        if self.params('f') and not self.params('e'):
            self.create_interrupted_path(self.x_size, self.y_size)

    # verringert auf allen kanten die pheromonstärke nach den parametern
    def evaporate(self, evaporation, evap_type):
        for edge in self.edges:
            edge.evaporate(evaporation, evap_type)

    def add_food(self, number, maxamount, minamount):
        xylist = []
        for x in range(1, (self.x_size + 1)):
            for y in range(1, (self.y_size + 1)):
                if x != self.nest.get_x() and y != self.nest.get_y():
                    xylist.append((x, y))
        random.shuffle(xylist)
        sources = xylist[:number]
        for (x, y) in sources:
            self.nodes.get((x, y)).add_food(random.randint(minamount, maxamount))

    def create_edges(self, max_x, max_y, thickness):
        edges = []
        for (x, y) in self.nodes:
            me = self.nodes.get((x, y))
            if x < max_x and random.randint(1, 100) <= thickness:
                right = self.nodes.get(((x + 1), y))
                edges.append(Edge(me, right))
            if y < max_y and random.randint(1, 100) <= thickness:
                down = self.nodes.get((x, (y + 1)))
                edges.append(Edge(me, down))
        return edges

    def create_labyrinth_edges(self, x, y):
        edges = []
        currnode = self.nodes[(1, 1)]
        while len(currnode.edges) < 2:
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
        self.nodes[(a, b)].value = 0
        return self.nodes[(a, b)]

    def create_nodes(self):
        nodes = {}
        for x in range(1, self.x_size + 1):
            for y in range(1, self.y_size + 1):
                add_me = Node(0, [], x, y)
                nodes[(x, y)] = add_me
        return nodes

    def create_suboptimal_path(self):
        self.nest = self.nodes[(1, 1)]
        self.nodes[(1,1)].nest = 1
        self.nodes[(4, 3)].add_food(500)
        for edge in self.edges:
            if edge.has_nodes(self.nodes[(1,1)], self.nodes[(2,1)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(2,1)], self.nodes[(2,2)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(2,2)], self.nodes[(2,3)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(2,3)], self.nodes[(2,4)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(2,4)], self.nodes[(3, 4)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(3,4)], self.nodes[(4,4)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(4,4)], self.nodes[(4,3)]):
                edge.food_pheromone = 2


    def create_interrupted_path(self):
        self.nest = self.nodes[(1, 1)]
        self.nodes[(1,1)].nest = 1
        self.nodes[(4, 4)].add_food(500)
        for edge in self.edges:
            if edge.has_nodes(self.nodes[(1,1)], self.nodes[(2,1)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(2,1)], self.nodes[(2,2)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(2,2)], self.nodes[(2,3)]):
                edge.node1.edges.remove(edge)
                edge.node2.edges.remove(edge)
                self.edges.remove(edge)
            if edge.has_nodes(self.nodes[(2,3)], self.nodes[(2,4)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(2,4)], self.nodes[(3, 4)]):
                edge.food_pheromone = 2
            if edge.has_nodes(self.nodes[(3,4)], self.nodes[(4,4)]):
                edge.food_pheromone = 2
