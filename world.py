import sys
from graph import Graph
from ants import Ants
from random import Random
from random import randint


class World(object):
    graph_obj = None
    ants = None
    file = "params.txt" # str(sys.argv[1])

    def params(self, param):
        file_obj = open(self.file)
        for line in file_obj:
            name = line.partition(": ")[0]
            if name == param:
                file_obj.close()
                return int(line.split(": ")[1])
        file_obj.close()

    def populate(self):
        self.ants = []
        greediness = range(self.params("greediness"))
        greediness_food = range(self.params("greediness_food"))
        for i in range(self.params("count")):
            ant = Ants(self.graph_obj.nest, self.graph_obj.nest, self.graph_obj.nest, 0, 0, greediness, greediness_food)
            ant.attr = i
            self.ants.append(ant)

    def create_ant(self):
        if len(self.ants) >= self.params("count_total"):
            return
        probability_new_ant = self.params("probability_new_ant")
        if randint(0, 100) < probability_new_ant:
            greediness_food = range(self.params("greediness_food"))
            greediness = range(self.params("greediness"))
            ant = Ants(self.graph_obj.nest, self.graph_obj.nest, self.graph_obj.nest, 0, 0, greediness, greediness_food)
            self.ants.append(ant)

    def simulate_cycle(self):
        for ant in self.ants:
            ant.action()
        for ant in self.ants:
            ant.set_pheromone()
        self.create_ant()
        self.graph_obj.evaporate(self.params("evaporation"), self.params("evaporation_type"))

    def run(self):
        for (x, y) in self.graph_obj.nodes:
            print(str(x) + "," + str(y) + "|" + str(self.graph_obj.get_node(x, y).nest) + ': ' + str(self.graph_obj.get_node(x, y).food))
        print("--------------------------")

        for i in range(self.params("loops")):
            self.simulate_cycle()
            for (x, y) in self.graph_obj.nodes:
                count = 0
                for ant in self.ants:
                    if ant.currpos.get_x_y() == (x, y):
                        count += 1
                print(x, ",", y, "|", self.graph_obj.get_node(x, y).nest, "X:", count, ':', self.graph_obj.get_node(x, y).food)
            print("--------------------------")


def main():
    # self.file = params_file
    ant_world = World()
    ant_world.graph_obj = Graph(ant_world.file)
    ant_world.populate()
    ant_world.run()

if __name__ == "__main__":
    main()

