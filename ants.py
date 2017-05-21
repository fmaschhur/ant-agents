import random


class Ants(object):
    def __init__(self, nest, currpos, lastpos, carrfood, nestdist, greediness, greedfood):
        self.nest = nest  # jede Ameise sollte zugehörigkeit zum Nest kennen, da evtl mehrere Neste?
        self.currpos = currpos
        self.lastpos = lastpos
        self.carrfood = carrfood
        self.nestdist = nestdist
        self.greedfood = greedfood
        self.greediness = greediness

    def set_pheromone(self):
        pheromone = (2 / (self.nestdist + 1.5))  # super krasse funktion
        if self.currpos != self.lastpos:
            if self.carrfood:
                self.currpos.set_pheromone(self.lastpos, pheromone, 0)
            else:
                self.currpos.set_pheromone(self.lastpos, 0, pheromone)

    def best_food_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            print("IF YOU READ THIS YOU FUCKED UP")
            return self.lastpos
        elif edges[0].food_pheromone == 0 or random.randint(1, 100) > self.greediness:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

    def best_nest_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.nest_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            print("IF YOU READ THIS YOU FUCKED UP")
            return self.lastpos
        elif edges[0].nest_pheromone == 0 or random.randint(1, 100) > self.greediness:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

    def change_pos(self, new_pos):
        self.lastpos = self.currpos
        self.currpos = new_pos
        self.nestdist += 1

    def collect_food(self):
        self.currpos.food -= 1
        self.carrfood += 1
        self.nestdist = 0
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

    def __init__(self, nest, currpos, lastpos, carrfood, nestdist, greediness):
        self.nest = nest  # jede Ameise sollte zugehörigkeit zum Nest kennen, da evtl mehrere Neste?
        self.currpos = currpos
        self.lastpos = lastpos
        self.carrfood = carrfood
        self.nestdist = nestdist
        self.greediness = greediness
        self.foundfood = 0

    def set_pheromone(self):
        pheromone = (2 / (self.nestdist + 1.5))  # super krasse funktion
        if self.foundfood:
            self.currpos.set_pheromone(self.lastpos, pheromone, 0)

    def best_food_node(self):


        edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            print("IF YOU READ THIS YOU FUCKED UP")
            return self.lastpos
        elif edges[0].food_pheromone == 0 or random.randint(1, 100) > self.greediness:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

    def best_nest_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.nest_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            print("IF YOU READ THIS YOU FUCKED UP")
            return self.lastpos
        elif edges[0].nest_pheromone == 0 or random.randint(1, 100) > self.greediness:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

    def change_pos(self, new_pos):
        self.lastpos = self.currpos
        self.currpos = new_pos
        self.nestdist += 1

    def action(self):
        pos = self.currpos
        if pos.food and not self.foundfood and not pos.nest:
            self.foundfood = 1
            self.change_pos(self.best_nest_node())
        elif pos.nest and self.foundfood:
            self.foundfood = 0
            self.change_pos(self.best_food_node())
        elif self.foundfood:
            self.change_pos(self.best_nest_node())
        else:
            self.change_pos(self.best_food_node())

class Carrier(object):

    def __init__(self, nest, currpos, lastpos, carrfood, nestdist, greedfood, greediness, allowed = False):
        self.nest = nest  # jede Ameise sollte zugehörigkeit zum Nest kennen, da evtl mehrere Neste?
        self.currpos = currpos
        self.lastpos = lastpos
        self.carrfood = carrfood
        self.nestdist = nestdist
        self.greedfood = greedfood
        self.greediness = greediness
        self.allowed = allowed

    def set_pheromone(self):
        pheromone = (2 / (self.nestdist + 1.5))  # super krasse funktion
        if self.currpos != self.lastpos:
            if self.carrfood:
                self.currpos.set_pheromone(self.lastpos, pheromone, 0)
            else:
                self.currpos.set_pheromone(self.lastpos, 0, pheromone)

    def best_food_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            print("IF YOU READ THIS YOU FUCKED UP")
            return self.lastpos
        elif edges[0].food_pheromone == 0 or random.randint(1, 100) > self.greediness:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

    def best_nest_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.nest_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            print("IF YOU READ THIS YOU FUCKED UP")
            return self.lastpos
        elif edges[0].nest_pheromone == 0 or random.randint(1, 100) > self.greediness:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

    def change_pos(self, new_pos):
        self.lastpos = self.currpos
        self.currpos = new_pos
        self.nestdist += 1

    def collect_food(self):
        self.currpos.food -= 1
        if self.currpos.food == 0:
            self.allowed == true
        self.carrfood += 1
        self.nestdist = 0
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
