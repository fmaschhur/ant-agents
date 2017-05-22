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

    def add_pheromone(self):
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

        if len(edges) == 1:
            print('fail')
            return edges[0].other_node(self.currpos)

        for i in range(len(edges)):
            if random.randint(1, 100) <= self.greediness:
                edges = list(filter(lambda x: x.food_pheromone == edges[i].food_pheromone, edges))
                return random.choice(edges).other_node(self.currpos)
        #edges[0].food_pheromone == 0 or random.randint(1, 100) > self.greediness:

        return random.choice(edges).other_node(self.currpos)

    def best_nest_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.nest_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            print("IF YOU READ THIS YOU FUCKED UP")
            return self.lastpos
        if edges[0].nest_pheromone == 0 or random.randint(1, 100) > self.greediness:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

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
            self.currpos.set_pheromone_2(self.lastpos, 1 / self.pheroz)

    def set_nodes(self):
        self.currpos.set_nestdist(self.currpos.smallest_nestdist_to_field())

    def best_food_node(self):
        # Wenn es essen gibt, was verbessert werden kann
        food_nodes = list(filter(lambda x: x.food != 0 or x.value > (self.currpos.value + 1), self.currpos.neighbours()))
        if food_nodes:
            return random.choice(food_nodes)
        # Erster Zug, wenn es keine Nachbarn mit Werten gibt
        if not self.currpos.highest_neighbour():
            return random.choice(self.currpos.neighbours_not_visited())
        # wenn es nur ein Nachbar gibt
        if len(self.currpos.neighbours()) == 1:
            return self.currpos.neighbours()[0]
        # Wenn kein Nachbar verbessert werden kann und es nicht besuchte Nachbarn gibt
        if self.currpos.highest_neighbour().value <= (self.currpos.value + 1) and self.currpos.neighbours_not_visited():
            return random.choice(self.currpos.neighbours_not_visited())
        # Damit nicht zurück gelaufen wird (Randfall)
        if self.currpos.highest_neighbour() == self.lastpos:
            print(len(self.currpos.neighbours()))
            asd = self.currpos.neighbours()
            asd.remove(self.currpos.highest_neighbour())
            return random.choice(asd)
        # laufe zum stärksten Nachbar
        return self.currpos.highest_neighbour()

    def best_nest_node(self):
        return self.currpos.smallest_neighbour()

    def change_pos(self, new_pos):
        self.lastpos = self.currpos
        self.currpos = new_pos

    def action(self):
        pos = self.currpos
        if pos.food and not self.foundfood and not pos.nest:
            self.foundfood = 1
            self.pheroz = self.currpos.value
        elif pos.nest and self.foundfood:
            self.pheroz = 0
            self.foundfood = 0

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

    def modify_pheromone(self, new_value):
        if self.currpos != self.lastpos:
            self.currpos.set_pheromone(self.lastpos, new_value, 0)

    def best_node(self):
        edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            return self.lastpos
        else:
            edges = list(filter(lambda x: x.food_pheromone == edges[0].food_pheromone, edges))
            return random.choice(edges).other_node(self.currpos)

    # def best_nest_node(self):
    #     edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
    #     for edge in edges:
    #         if edge.other_node(self.currpos) == self.lastpos:
    #             edges.remove(edge)
    #     if not edges:
    #         return self.lastpos
    #     else:
    #         edges = list(filter(lambda x: x.food_pheromone == edges[0].food_pheromone, edges))
    #         return random.choice(edges).other_node(self.currpos)

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
        elif self.pheromone_modification:
            edges = sorted(self.currpos.edges, key=lambda x: x.food_pheromone, reverse=True)
            self.change_pos(self.best_node())
            self.modify_pheromone(edges[1].food_pheromone) # diiiiirdy quick-fix
        else:
            self.change_pos(self.best_node())
