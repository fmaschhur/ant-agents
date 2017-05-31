from deal import Deal
from graph import Graph

# Knoten und, wenn auf grade auf einer Edge dann abstand vom Knoten
class Position(object):
    def __init__(self, start):
        self.node = start
        self.edge = None
        self.distance = 0  # distance on edge
