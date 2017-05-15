class Edge(object):

    def init(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.food_pheromone = None
        self.nest_pheromone = None
