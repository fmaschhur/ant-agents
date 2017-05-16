class Ant(object):
    def __init__(self, currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
        self.currpos = currpos
        self.lastpos = lastpos
        self.carrfood = carrfood
        self.nestdist = nestdist
        self.greedfood = greedfood
        self.greedpherom = greedpherom

    def set_pheromone(self):
        pheromon = (1 / self.nestdist)  # super krasse funktion
        # wird die nestdist auf 0 gesetzt wenn futter gefunden wurde? würde es einfacher machen ;)
        if self.carrfood:
            self.currpos.set_pheromone(self.lastpos, pheromon, 0)
        else:
            self.currpos.set_pheromone(self.lastpos, 0, pheromon)

    def best_edge_food(self):
        edgetogo = None
        for edge in self.currpos.edges:
            if edgetogo == None:
                edgetogo = edge
            if edge.food_pheromone > edgetogo.food_pheromone:
                edgetogo = edge

    def best_edge_nest(self):
        edgetogo = None
        for edge in self.currpos.edges:
            if edgetogo == None:
                edgetogo = edge
            if edge.food_pheromone > edgetogo.food_pheromone:
                edgetogo = edge

    def change_pos(self, new_pos):
            self.lastpos = self.currpos
            self.currpos = new_pos
            self.nestdist += 1

    def collect_food(self):
        self.currpos.food -= 1
        self.carrfood += 1
        self.nestdist = 0

    def drop_food_in_nest(self):
            self.currpos.food += 1
            self.carrfood -= 1
            self.nestdist = 0



    def action(self):
        pos = self.currpos
        if pos.food and not self.carrfood:  # food != 0 ist == food
            self.collect_food()
        elif pos.nest:
            self.drop_food_in_nest()
        elif self.carrfood:
            self.change_pos(self.best_edge_nest)

        else:
            self.change_pos(self.best_edge_nest)






    def action_old(self):

        if self.currpos.food > 0 and self.carrfood == 0:  # first possibility to take food if there is some and ant is not carrying smth
            self.currpos.food -= 1  # that is happening in 1 cycle, and in each cycle theres one action() function call done right?
            self.carrfood += 1
        else:  # if ant has already food or there is none then it should move
            if self.carrfood == 0:

                # TODO: random choice of edge if there are no existing pheromons
                # TODO: also let the both greedinesses factor influence the behavior of moving
                edgetogo = None
                for edge in self.currpos.edges:
                    if edge.food_pheromone > tmp.food_pheromone:
                        edgetogo = edge

                lastpos = currpos
                self.setnestpherom(edgetogo)
                self.nestdist += 1

                if: lastpos == edgetogo.node1
                currpos = edgetogo.node2
            else:
                currpos = edgetogo.node1

        elif self.carrfood == 1:
        edgetogo = None
        for edge in self.currpos.edges:
            if edge.nest_pheromone > tmp.nest_pheromone:
                edgetogo = edge

        lastpos = currpos
        self.setfoodpherom(edgetogo)
        self.nestdist = - 1
        if: lastpos == edgetogo.node1
        currpos = edgetogo.node2

    else:
    currpos = edgetogo.node1


def setfoodpherom(edge):
    # TODO: amount of pheromons has to be influenced by time
    # edge.foodpherom = xx
    pass


def setnestpherom(selfedge):
    # TODO: amount of pheromons has to be influenced by time
    # edge.nestpherom = xx
    pass

# TODO: Exercise 2: different types of ants
# class Explorer(Ant):

#   def init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
#      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)

# class Carrier(Ant):

#   def init(self, currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
#      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)


