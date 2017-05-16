import sys
import graph
import ants
import random


graph = None
ants = None
file = str(sys.argv[1])


def params(self, param):
    file_obj = open(self.file)
    for line in file_obj:
        name = line.partition(': ')[0]
        if name == param:
            file_obj.close()
            return int(line.partition(': ')[1])
    file_obj.close()


def populate(self):
    self.ants = []
    greediness = range(params('greediness'))
    greediness_food = range(params('greediness_food'))
    for i in range(params('count')):
        ant = ants.init(self.graph.nest, self.graph.nest, 0, 0, greediness, greediness_food)
        ant.attr = i
        self.ants.append(ant)


def create_ant(self):
    if self.ants.size >= params('count_total'):
        return
    probability_new_ant = range(params('probability_new_ant'))
    if random.randint(0, 100) < probability_new_ant:
        greediness_food = range(params('greediness_food'))
        greediness = range(params('greediness'))
        ant = ants.init(self.graph.nest, self.graph.nest, 0, 0, greediness, greediness_food)
        self.ants.append(ant)


def simulate_cycle(self):
    create_ant()
    for ant in self.ants:
        ant.action()
    for ant in self.ants:
        ant.set_pheromon()
    self.graph.evaporate(params('evaporation'), params('evaporation_type'))


def run():
    for i in range(params('loops')):
        simulate_cycle()


def main(self):
    self.graph = graph.init(self.file)
    populate()
    run()
