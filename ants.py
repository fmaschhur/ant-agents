class Ant(object):

    def init(self, currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
        self.currpos = currpos
        self.lastpos = lastpos
        self.carrfood = carrfood
        self.nestdist = nestdist
        self.greedfood = greedfood
        self.greedpherom = greedpherom

    def action():

        if currpos.food > 0 and self.carrfood == 0:         # first possibility to take food if there is some and ant is not carrying smth
            self.Currpos.food -= 1                          # that is happening in 1 cycle, and in each cycle theres one action() function call done right?
            self.Carrfood += 1
        else:                                               #if ant has already food or there is none then it should move
            if self.carrfood == 0:

                #TODO: random choice of edge if there are no existing pheromons
                #TODO: also let the both greedinesses factor influence the behavior of moving
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

            elif self.Carrfood == 1:
                edgetogo = None
                for edge in self.currpos.edges:
                    if edge.nest_pheromone > tmp.nest_pheromone:
                        edgetogo = edge

                lastpos = currpos
                self.setfoodpherom(edgetogo)
                self.nestdist =- 1
                if: lastpos == edgetogo.node1
                    currpos = edgetogo.node2
                else:
                    currpos = edgetogo.node1


    def setfoodpherom(edge):
        #TODO: amount of pheromons has to be influenced by time
        #edge.foodpherom = xx
        pass
    def setnestpherom(selfedge):
        #TODO: amount of pheromons has to be influenced by time
        #edge.nestpherom = xx
        pass

#TODO: Exercise 2: different types of ants
#class Explorer(Ant):

 #   def init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
  #      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)

#class Carrier(Ant):

 #   def init(self, currpos, lastpos, carrfood, nestdist, greedfood, greedpherom):
  #      Ant.init(self,currpos, lastpos, carrfood, nestdist, greedfood, greedpherom)


