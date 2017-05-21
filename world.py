import sys
from graph import Graph
from ants import Ants
from ants import Explorer
from ants import Carrier
from random import Random
from random import randint
from time import sleep
from logger import Logger


class World(object):
    graph = None
    ants = None
    explorer = None
    carrier = None

    def __init__(self, params):
        self.ant_greediness = params['greediness']
        self.ant_greediness_food = params['greediness_food']
        self.ants_init = params['ants_init']
        self.ants_max = params['ants_max']
        self.probability_new_ant = params['probability_new_ant']
        self.evaporation = params['evaporation']
        self.evaporation_type = params['evaporation_type']
        self.wait = params['wait']

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
        sleep(self.wait)
        for ant in self.ants:
            ant.action()
        for ant in self.ants:
            ant.set_pheromone()
        self.create_ant()
        self.graph.evaporate(self.evaporation, self.evaporation_type)

    def simulate_cycle_explorer_carrier(self):
        sleep(self.wait)
        for explorer in self.explorer:
            explorer.action()
            explorer.action()
        for explorer in self.explorer:
            if explorer.carrfood == True:
                explorer.set_pheromone()

        for carrier in self.carrier:
            for edges in carrier.currpos.edges:
                if edge.food_pheromone > 0:
                    go = True
            if go == True:
                carrier.action()

        self.create_ant()
        self.graph.evaporate(self.evaporation, self.evaporation_type)
