import random


class Node(object):

    def __init__(self, food, edges):    # initializes a single node and associates a list of edges to it
        self.food = food            # int, x if nest, 0 else
        self.edges = edges          # list of edges, can be empty, argument has to be 'None' for this to happen
        self.nest = 0               # Muss das wissen damit die Ameisen das ohne auf den graphen zuzugreifen wissen können

    def add_food(self, amount, probability):
        if random() < (probability * 0.01):
            self.food = amount

    def set_pheromone(self, coming_from, food, nest):
            for edge in self.edges:
                if edge.node2 == coming_from:
                    edge.set_pheromon(food, nest)
                    for edge2 in edge.node2.edges:
                        if edge2.node2 == self:
                            edge2.set_pheromon(food, nest)

    def has_food(self):
        return self.food > 0
