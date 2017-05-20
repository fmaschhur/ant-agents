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
        pheromone = (1 / (self.nestdist + 1))  # super krasse funktion
        if self.currpos != self.lastpos:
            if self.carrfood:
                self.currpos.set_pheromone(self.lastpos, pheromone, 0)
            else:
                self.currpos.set_pheromone(self.lastpos, 0, pheromone)

    def best_food_node(self):
        # edgetogo = None
        # for edge in self.currpos.edges:
        #     if edgetogo is None:
        #         if edge.other_node(self.currpos) != self.lastpos:
        #             edgetogo = edge
        #     elif (edge.food_pheromone > edgetogo.food_pheromone or random.randint(1, 100) > self.greediness) and edge.other_node(self.currpos) != self.lastpos:
        #         edgetogo = edge
        # # print(edgetogo.node1.get_x_y(), edgetogo.node2.get_x_y())
        # if edgetogo is None:
        #     edgetogo = self.currpos.edges[0]
        # return edgetogo.other_node(self.currpos)
        edges = sorted(self.currpos.edges, key=lambda x:x.food_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            return self.currpos.edges[0].other_node(self.currpos)
        elif edges[0].food_pheromone == 0:
            return random.choice(edges).other_node(self.currpos)
        else:
            return edges[0].other_node(self.currpos)

    def best_nest_node(self):
        # edgetogo = None
        # print("Current Position Edges go to:")
        # for edge in self.currpos.edges:
        #     print(edge.other_node(self.currpos).get_x_y())
        #     if edgetogo is None:
        #         if edge.other_node(self.currpos) != self.lastpos:
        #             edgetogo = edge
        #     elif (edge.nest_pheromone > edgetogo.nest_pheromone or random.randint(1, 100) > self.greediness) and edge.other_node(self.currpos) != self.lastpos:
        #         edgetogo = edge
        # if edgetogo is None:
        #     edgetogo = self.currpos.edges[0]
        # return edgetogo.other_node(self.currpos)
        edges = sorted(self.currpos.edges, key=lambda x: x.nest_pheromone, reverse=True)
        for edge in edges:
            if edge.other_node(self.currpos) == self.lastpos:
                edges.remove(edge)
        if not edges:
            return self.currpos.edges[0].other_node(self.currpos)
        elif edges[0].nest_pheromone == 0:
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
        if pos.food and not self.carrfood and not pos.nest:  # food != 0 ist == food
            self.collect_food()
        elif pos.nest and self.carrfood:
            self.drop_food_in_nest()
        elif self.carrfood:
            self.change_pos(self.best_nest_node())
        else:
            self.change_pos(self.best_food_node())

#
#
#
#     def action_old(self):
#
#         if self.currpos.food > 0 and self.carrfood == 0:  # first possibility to take food if there is some and ant is not carrying smth
#             self.currpos.food -= 1  # that is happening in 1 cycle, and in each cycle theres one action() function call done right?
#             self.carrfood += 1
#         else:  # if ant has already food or there is none then it should move
#             if self.carrfood == 0:
#
#                 # TODO: random choice of edge if there are no existing pheromons
#                 # TODO: also let the both greedinesses factor influence the behavior of moving
#                 edgetogo = None
#                 for edge in self.currpos.edges:
#                     if edge.food_pheromone > tmp.food_pheromone:
#                         edgetogo = edge
#
#                 lastpos = currpos
#                 self.setnestpherom(edgetogo)
#                 self.nestdist += 1
#
#                 if: lastpos == edgetogo.node1
#                 currpos = edgetogo.node2
#             else:
#                 currpos = edgetogo.node1
#
#         elif self.carrfood == 1:
#         edgetogo = None
#         for edge in self.currpos.edges:
#             if edge.nest_pheromone > tmp.nest_pheromone:
#                 edgetogo = edge
#
#         lastpos = currpos
#         self.setfoodpherom(edgetogo)
#         self.nestdist = - 1
#         if: lastpos == edgetogo.node1
#         currpos = edgetogo.node2
#
#     else:
#     currpos = edgetogo.node1
#
#
# def setfoodpherom(edge):
#     # TODO: amount of pheromons has to be influenced by time
#     # edge.foodpherom = xx
#     pass
#
#
# def setnestpherom(selfedge):
#     # TODO: amount of pheromons has to be influenced by time
#     # edge.nestpherom = xx
#     pass

# TODO: Exercise 2: different types of ants
# class Explorer(Ant):

#   def init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
#      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)

# class Carrier(Ant):

#   def init(self, currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
#      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)
