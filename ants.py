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
        pheromone = (5 / (self.nestdist + 5))  # super krasse funktion
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

# TODO: Exercise 2: different types of ants
# class Explorer(Ant):

#   def init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
#      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)

# class Carrier(Ant):

#   def init(self, currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
#      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)
