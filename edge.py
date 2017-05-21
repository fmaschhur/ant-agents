class Edge(object):
    def __init__(self, node1, node2):  # initialises an edge given 2 (different) nodes, order doesn't matter
        self.node1 = node1  # first node
        self.node2 = node2  # second node
        self.food_pheromone = 0.0  # float food pheromone, empty
        self.nest_pheromone = 0.0  # float nest pheromone, empty
        node1.edges.append(self)  # save edge in nodes
        node2.edges.append(self)  #

    def evaporate(self, evaporation, evap_type):
        if evap_type == 1:
            if self.food_pheromone - evaporation < 0.0:
                self.food_pheromone = 0.0
            else:
                self.food_pheromone -= evaporation
            if self.nest_pheromone - evaporation < 0.0:
                self.nest_pheromone = 0.0
            else:
                self.nest_pheromone -= evaporation
        elif evap_type == 2:
            if self.food_pheromone < 0.005:
                self.food_pheromone = 0.0
            else:
                self.food_pheromone *= evaporation * 0.01
            if self.nest_pheromone < 0.005:
                self.nest_pheromone = 0.0
            else:
                self.nest_pheromone *= evaporation * 0.01

    def set_pheromone(self, food, nest):
        self.food_pheromone += food
        self.nest_pheromone += nest

    def get_food_pheromone(self):
        return self.food_pheromone

    def get_nest_pheromone(self):
        return self.nest_pheromone

    def has_nodes(self, node1, node2):  # falls node1, node2 die Nodes der Kante sind return true
        return ((self.node1 == node1 and self.node2 == node2) or (self.node1 == node2 and self.node2 == node1))

    def has_node(self, node):  # falls node einer der beiden Nodes der Kante ist return true
        return (self.node1 == node or self.node2 == node)

    def connected_nodes(self):
        return (self.node1, self.node2)

    def other_node(self, node):
        if node == self.node1:
            return self.node2
        elif node == self.node2:
            return self.node1
        else:
            return None
