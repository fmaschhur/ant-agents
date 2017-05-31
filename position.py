from deal import Deal
from graph import Graph


class Position(object):
    def __init__(self, start):
        self.node = start
        self.edge = None
        self.distance = 0  # distance on edge
