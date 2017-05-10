import sys
import graph
import ants


graph = None
nest = None
ants = None
file = ''


def params(param):
    file_obj = open(file)
    for line in file_obj:
        name = line.partition(': ')[0]
        if name == param:
            file_obj.close()
            return int(line.partition(': ')[1])
    file_obj.close()


def generate_world():
    graph = Graph.init(params('graph'))


def populate():
    ants = []
    greediness = range(params('greediness'))
    greediness_food = range(params('greediness_food'))
    for i in range(params('count')):
        ant = ants.init(nest, nest, 0, 0, greediness, greediness_food)
        ant.attr = i
        ants.append(ant)

def create_ants_in_run():



def simulate_cycle():
    create_ants_in_run()
    for ant in ants:
        ant.action()
    for ant in ants:
        ant.set_pheromon()
    graph.evaporate(params('evaporation'))



def run():
    for i in range(params('loops')):
        simulate_cycle()


def main():
    file = str(sys.argv[1])
    generate_world()
    populate()
    run()
