import sys
import graph
import ant


def params(file, param):
    file_obj = open(file)
    for line in file_obj:
        name = line.partition(': ')[0]
        if name == param:
            file_obj.close()
            return int(line.partition(': ')[1])
    file_obj.close()


def generate_world(file):
    return Graph(params(file, 'graph'))


def populate(file):
    ants = []
    greediness = range(params(file, 'greediness'))
    greediness_food = range(params(file, 'greediness_food'))
    for i in range(params(file, 'count')):
        ant = Ant(greediness, greediness_food)
        ant.attr = i
        ants.append(ant)
    return ants

def create_ants_in_run(birth_time, ants):



def simulate_cycle(file, ants, graph):
    create_ants_in_run(params(file, 'birth_time'), ants)
    for ant in ants:
        ant.action()
    for ant in ants:
        ant.set_pheromon()
    graph.evaporate(params(file, 'evaporation'))



def run(file, ants, graph):
    for i in range(params(file, 'loops')):
        simulate_cycle(file, ants, graph)


def main():
    file = str(sys.argv[1])

    graph = generate_world(file)
    ants = populate(file)
    run(file, ants, graph)
