import sys
from graph import Graph
from ants import Ants
from random import Random
from random import randint
from time import sleep
from logger import Logger


class World(object):
    graph = None
    ants = None

    def __init__(self, params):
        self.ant_greediness = params['greediness']
        self.ant_greediness_food = params['greediness_food']
        self.ants_init = params['ants_init']
        self.ants_max = params['ants_max']
        self.probability_new_ant = params['probability_new_ant']
        self.evaporation = params['evaporation']
        self.evaporation_type = params['evaporation_type']

    def populate(self):
        self.ants = []
        for i in range(self.ants_init):
            ant = Ants(self.graph.nest, self.graph.nest, self.graph.nest, 0, 0, self.ant_greediness,
                       self.ant_greediness_food)
            ant.attr = i
            self.ants.append(ant)

    def create_ant(self):
        if len(self.ants) >= self.ants_max:
            return
        if randint(0, 100) < self.probability_new_ant:
            ant = Ants(self.graph.nest, self.graph.nest, self.graph.nest, 0, 0, self.ant_greediness,
                       self.ant_greediness_food)
            self.ants.append(ant)

    def simulate_cycle(self):
        sleep(0.5)
        for ant in self.ants:
            ant.action()
        for ant in self.ants:
            ant.set_pheromone()
        self.create_ant()
        self.graph.evaporate(self.evaporation, self.evaporation_type)
