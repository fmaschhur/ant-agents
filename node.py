import random


class Node(object):

    def __init__(self, food, edges, x_pos, y_pos):    # initializes a single node and associates a list of edges to it
        self.food = food            # int, x if nest, 0 else
        self.edges = edges          # list of edges, can be empty, argument has to be 'None' for this to happen
        self.x_pos = x_pos            # x position
        self.y_pos = y_pos               # y position
        self.nest = 0               # Muss das wissen damit die Ameisen das ohne auf den graphen zuzugreifen wissen können

    def add_food(self, amount, probability):
        if random.randint(0, 100) < probability:
            self.food = amount

    def set_pheromone(self, coming_from, food, nest):
            for edge in self.edges:
                if edge.has_node(coming_from):
                    edge.set_pheromone(food, nest)

    def has_food(self):
        return self.food > 0

    def get_x(self):        # funktion zum abfragen der x position
        return self.xpos
    #
    def get_y(self):        # funktion zum abfragen der y position
        return self.ypos
    #
    # def get_x_y(self):      # funktion zum abfragen der x und y positionen
    #     return (self.xpos, self.ypos)