class Edge(object):

    def __init__(self, node1, node2):       # initialises an edge given 2 (different) nodes, order doesn't matter
        self.node1 = node1              # first node
        self.node2 = node2              # second node
        self.food_pheromone = None      # float food pheromone, empty
        self.nest_pheromone = None      # float nest pheromone, empty

