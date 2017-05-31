import random
import math
from operator import truediv


class Job(object):
    def __init__(self, id, time, destination):
        self.id = id
        self.time = time
        self.destination = destination
        self.status = 0
        self.initiator = None


