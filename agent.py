from deal import Deal
from graph import Graph


class Agent(object):
    def __init__(self, id, position, capacity, speed, preferences, reload_time):
        self.id = id
        self.position = Position(position)
        self.max_capacity = capacity
        self.capacity = capacity
        self.reload_time = reload_time
        self.speed = speed
        self.preferences = preferences
        self.deals = None #TODO frage: fahren die Agenten schon los wenn sie ein pre bid gesetzt haben?

    def move(self, graph): #TODO  frage: soll der agent direkt weiter fahren oder bleibt er wenn ein ziel erreicht ist stehen?
        if not self.deals:
            return
        pos = self.position
        dest = self.deals[0].job.destination

        if self.capacity <= 0:
            if abs(self.capacity) >= reload_time:
                self.capacity = self.max_capacity
            self.capacity -= 1
        elif graph.get_distance(pos, dest) <= speed:
            self.position = Position(dest)
            self.deals.pop.jobs.status = 3
        else:
            self.position = graph.get_position_from_position(pos, dest, speed)

    def new_deals(self, new_jobs):
        first_change = None
        if self.deals:
            for i, deal in enumerate(self.deals):
                if deal.is_definitive_rejected():
                    if first_change is None:
                        first_change = i - 1
                    deals.remove(deal)
        new_deals = set(new_jobs).intersection(self.preferences)
        new_deals = list(map(lambda x: Deal(self, x), new_deals))
        if new_deals:
            self.deals.extend(new_deals)
        print(new_jobs)
        #TODO wie erreichen wir alle deals abhängig von präferenz in möglichst kurzer zeit ohne dass ein deal langsamer wird als vorher?
        #TODO #superComplicated


class Position(object):
    def __init__(self, start):
        self.node = start
        self.edge = None
        self.distance = 0  # distance on edge
