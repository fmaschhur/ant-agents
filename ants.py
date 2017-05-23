import random
from math import inf


class Ants(object):
    def __init__(self, nest, currpos, lastpos, carrfood, nestdist, greediness, greedfood):
        self.nest = nest  # jede Ameise sollte zugehörigkeit zum Nest kennen, da evtl mehrere Neste?
        self.currpos = currpos
        self.lastpos = lastpos
        self.carrfood = carrfood
        self.nestdist = nestdist
        self.greedfood = greedfood
        self.greediness = greediness

    def add_pheromone(self):
        pheromone = (2 / (self.nestdist + 1.5))  # super krasse funktion
        if self.currpos != self.lastpos:
            if self.carrfood:
                self.currpos.add_pheromone(self.lastpos, pheromone, 0)
            else:
                self.currpos.add_pheromone(self.lastpos, 0, pheromone)

    def best_food_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            return self.lastpos
        if self.greediness == 100:
            return random.choice(list(filter(lambda x: x.food_pheromone == edges[0].food_pheromone, edges))).other_node(
                self.currpos)
        x = random.randint(1, 100)
        values = []
        minisum = 0
        for i in range(len(edges)):
            for j in range(i):
                if j != i:
                    minisum += values[j]
                else:
                    minisum += self.get_probability(edges[j], edges, 'food')
            values.append(minisum)
        for i in range(len(values)):
            if values[i] <= x:
                return edges[i].other_node(self.currpos)

    def best_nest_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.nest_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            return self.lastpos
        if self.greediness == 100:
            return random.choice(list(filter(lambda x: x.nest_pheromone == edges[0].nest_pheromone, edges))).other_node(self.currpos)
        x = random.randint(1, 100)
        values = []
        minisum = 0
        for i in range(len(edges)):
            for j in range(i):
                if j != i:
                    minisum += values[j]
                else:
                    minisum += self.get_probability(edges[j], edges, 'nest')
            values.append(minisum)
        for i in range(len(values)):
            if values[i] <= x:
                return edges[i].other_node(self.currpos)

    def get_probability(self, edge, edges, type):
        if type == 'nest':
            sum_pheromone = 0
            sum_probability = 0
            p = 0
            for i in range(len(edges)):
                x = (edge.nest_pheromone * math.pow((self.greediness/10), 2))/sum + ((100-self.greediness)/len(edges))
                if edges[i] == edge:
                    p = x
                sum_pheromone += edge.nest_pheromone
                sum_probability += x
            return 100*(p/sum_probability)
        if type == 'food':
            sum_pheromone = 0
            sum_probability = 0
            p = 0
            for i in range(len(edges)):
                x = (edge.food_pheromone * math.pow((self.greediness/10), 2))/sum + ((100-self.greediness)/len(edges))
                if edges[i] == edge:
                    p = x
                sum_pheromone += edge.food_pheromone
                sum_probability += x
            return 100*(p/sum_probability)

    def change_pos(self, new_pos):
        if self.currpos.nest:
            self.nestdist = 0
            self.currpos = new_pos
            self.lastpos = self.currpos
            return
        self.nestdist += 1
        self.lastpos = self.currpos
        self.currpos = new_pos

    def collect_food(self):
        self.currpos.food -= 1
        self.carrfood += 1
        self.lastpos = self.currpos

    def drop_food_in_nest(self):
        self.currpos.food += 1
        self.carrfood -= 1
        self.nestdist = 0
        self.lastpos = self.currpos

    def action(self):
        pos = self.currpos
        if pos.food and not self.carrfood and not pos.nest and random.randint(1, 100) <= self.greedfood:
            self.collect_food()
        elif pos.nest and self.carrfood:
            self.drop_food_in_nest()
        elif self.carrfood:
            self.change_pos(self.best_nest_node())
        else:
            self.change_pos(self.best_food_node())


class Explorer(object):

    def __init__(self, nest, currpos, lastpos, foundfood):
        self.nest = nest  # jede Ameise sollte zugehörigkeit zum Nest kennen, da evtl mehrere Neste?
        self.currpos = currpos
        self.lastpos = lastpos
        self.foundfood = foundfood
        self.pheroz = 0

    def set_pheromone(self):
        if self.foundfood:
            pheromone = 1 / (self.pheroz + 10) + 1 / (self.currpos.value + 1)

            self.currpos.set_pheromone_2(self.lastpos, pheromone)

    def set_nodes(self):
        self.currpos.set_nestdist(self.currpos.smallest_nestdist_to_field())

    # Nachbar, mit essen, dass verbessert werden kann
    def food_in_area(self):
        food_nodes = list(filter(lambda x: x.food != 0 and (x.value == inf or x.value > (self.currpos.value + 1)), self.currpos.neighbours()))
        if food_nodes:
            return random.choice(food_nodes)
        return False

    def best_food_node(self):
        pos = self.currpos
        highest_neighbour = pos.highest_neighbour()
        food_nodes = list(filter(lambda x: x.food != 0 and not x.nest, self.currpos.neighbours()))
        if food_nodes:
            return random.choice(food_nodes)

        if pos.neighbours_not_visited():
            return random.choice(pos.neighbours_not_visited())

        if highest_neighbour.value >= (pos.value + 1) and highest_neighbour.not_equal(self.lastpos):
            return highest_neighbour

        return random.choice(pos.neighbours())

    def best_nest_node(self):
        edges = []
        for node in self.currpos.smallest_neighbours():
            edges += node.edges
        print(edges)
  #      edges = list(map(lambda x: x.edges, edges))
        print(edges)
        edges = list(filter(lambda x: x.has_node(self.currpos), edges))
        edges = list(sorted(edges, key=lambda x: x.food_pheromone, reverse=True))
        return list(map(lambda x: x.other_node(self.currpos), edges))[0]

    def change_pos(self, new_pos):
        self.lastpos = self.currpos
        self.currpos = new_pos

    def action(self):
        pos = self.currpos
        if pos.food and not self.foundfood and not pos.nest:
            self.foundfood = 1
            self.pheroz = self.currpos.value
            self.lastpos = pos
            self.currpos = pos
        elif pos.nest:
            self.pheroz = 0
            self.foundfood = 0
            self.lastpos = pos
            self.currpos = pos

        if self.foundfood:
            self.change_pos(self.best_nest_node())
        else:
            self.change_pos(self.best_food_node())

        self.set_pheromone()


class Carrier(object):

    def __init__(self, nest, currpos, lastpos, carrfood, pheromone_modification):
        self.nest = nest  # jede Ameise sollte zugehörigkeit zum Nest kennen, da evtl mehrere Neste?
        self.currpos = currpos
        self.lastpos = lastpos
        self.carrfood = carrfood
        self.pheromone_modification = pheromone_modification

    def modify_pheromone(self):
        if self.currpos != self.lastpos:
            self.currpos.set_pheromone(self.lastpos, 0, 0)

    def best_nest_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            return self.lastpos
        else:
            edges = list(filter(lambda x: x.food_pheromone == edges[0].food_pheromone, edges))
            return random.choice(edges).other_node(self.currpos)

    def best_food_node(self):
        last_edge = None
        edges = self.currpos.edges
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                last_edge = edge
        if last_edge is not None:
            edges = list(filter(lambda x: x.food_pheromone < last_edge.food_pheromone, edges))
        # if not edges:
        #      return self.lastpos
        # else:
            edges = sorted(edges, key=lambda x: x.food_pheromone, reverse=True)
            edges = list(filter(lambda x: x.food_pheromone == edges[0].food_pheromone, edges))
            return random.choice(edges).other_node(self.currpos)

    def change_pos(self, new_pos):
        self.lastpos = self.currpos
        self.currpos = new_pos

    def collect_food(self):
        self.currpos.food -= 1
        if self.currpos.food == 0:
            self.pheromone_modification = True
        self.carrfood = True
        self.lastpos = self.currpos

    def drop_food_in_nest(self):
        self.currpos.food += 1
        self.carrfood = False
        self.lastpos = self.currpos
        self.pheromone_modification = False

    def action(self):
        pos = self.currpos
        if pos.food and not self.carrfood and not pos.nest:
            self.collect_food()
        elif pos.nest and self.carrfood:
            self.drop_food_in_nest()
        # elif self.pheromone_modification:
        #     edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
        #     self.change_pos(self.best_node())
        #     self.modify_pheromone(edges[1].food_pheromone) # diiiiirdy quick-fix
        elif not pos.nest and self.carrfood:
            self.change_pos(self.best_nest_node())
        else:
            self.change_pos(self.best_food_node())

