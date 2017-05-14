import sys
import graph
import ants
import random


Graph = None
Nest = None
Ants = None
File = str(sys.argv[1])


def params(self, param, float_return):
    file_obj = open(self.File)
    for line in file_obj:
        name = line.partition(': ')[0]
        if name == param:
            file_obj.close()
            return int(line.partition(': ')[1])
    file_obj.close()


def populate(self):
    self.Ants = []
    greediness = range(params('greediness'))
    greediness_food = range(params('greediness_food'))
    for i in range(params('count')):
        ant = ants.init(self.Nest, self.Nest, 0, 0, greediness, greediness_food)
        ant.attr = i
        self.Ants.append(ant)


def create_ant(self):
    if self.Ants.size >= params('count_total'):
        return
    probability_new_ant = range(params('probability_new_ant'))
    if random.randint(0, 100) < probability_new_ant:
        greediness_food = range(params('greediness_food'))
        greediness = range(params('greediness'))
        ant = ants.init(self.Nest, self.Nest, 0, 0, greediness, greediness_food)
        self.Ants.append(ant)


def simulate_cycle(self):
    create_ant()
    for ant in self.Ants:
        ant.action()
    for ant in self.Ants:
        ant.set_pheromon()
    graph.evaporate(params('evaporation'))


def run():
    for i in range(params('loops')):
        simulate_cycle()


def main(self):
    self.Graph = graph.init(params('graph'))
    populate()
    run()
