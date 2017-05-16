class Edge(object):

    def __init__(self, node1, node2):       # initialises an edge given 2 (different) nodes, order doesn't matter
        self.node1 = node1              # first node
        self.node2 = node2              # second node
        self.food_pheromone = 0.0      # float food pheromone, empty
        self.nest_pheromone = 0.0      # float nest pheromone, empty

    def evaporate(self, evaporation, evap_type):
        if evap_type == 1:
            self.food_pheromone -= evaporation
            self.nest_pheromone -= evaporation
        elif evap_type == 2:
            self.food_pheromone *= evaporation * 0.01
            self.nest_pheromone *= evaporation * 0.01

    def set_pheromone(self, food, nest):
        self.food_pheromone += food
        self.nest_pheromone += nest
