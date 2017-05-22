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
        self.explorer_greediness = params['greediness_explorers']
        self.carrier_greediness = params['greediness_carriers']
        self.explorer_greediness_food = params['greediness_explorers_food']
        self.carrier_greediness_food = params['greediness_carriers_food']
        self.ants_init = params['ants_init']
        self.ants_max = params['ants_max']
        self.carriers_init = params['carriers_init']
        self.explorer_init = params['explorers_init']
        self.explorers_max = params['explorers_max']
        self.carriers_max = params['carriers_max']
        self.probability_new_ant = params['probability_new_ant']
        self.probability_new_explorer = params['probability_new_explorer']
        self.probability_new_carrier = params['probability_new_carrier']
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

    def populate_explorers(self):
        self.explorers = []
        for i in range(self.explorer_init):
            explorer = Explorer(self.graph.nest, self.graph.nest, self.graph.nest, 0, 0, self.explorer_greediness,
                       self.explorer_greediness_food)
            explorer.attr = i
            self.explorers.append(explorer)

    def populate_carriers(self):
        self.carriers = []
        for i in range(self.carriers_init):
            carrier = Carrier(self.graph.nest, self.graph.nest, self.graph.nest, 0, 0, self.carrier_greediness,
                       self.carrier_greediness_food)
            carrier.attr = i
            self.carriers.append(carrier)

    def create_ant(self):
        if len(self.ants) >= self.ants_max:
            return
        if randint(0, 100) < self.probability_new_ant:
            ant = Ants(self.graph.nest, self.graph.nest, self.graph.nest, 0, 0, self.ant_greediness,
                       self.ant_greediness_food)
            self.ants.append(ant)

    def create_explorer(self):
        if len(self.explorers) >= self.explorers_max:
            return
        if randint(0, 100) < self.probability_new_explorer:
            explorer = Explorer(self.graph.nest, self.graph.nest, self.graph.nest, 0, 0, self.explorer_greediness,
                       self.explorer_greediness_food)
            self.explorers.append(explorer)

    def create_carrier(self):
        if len(self.carriers) >= self.carriers_max:
            return
        if randint(0, 100) < self.probability_new_carrier:
            carrier = Carrier(self.graph.nest, self.graph.nest, self.graph.nest, 0, 0, self.carrier_greediness,
                       self.carrier_greediness_food)
            self.carriers.append(carrier)
#

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
            if carrier.allowed == True
                #carrier.set_pheromone()        Food gefunden, dann auf dem Rückweg Pheromonspur manipulieren

        self.create_ant()
        self.graph.evaporate(self.evaporation, self.evaporation_type)
