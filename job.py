import random
import math
from operator import truediv


class Job(object):
    def __init__(self, id, time, destination):
        self.id = id
        self.time = time
        self.destination = destination
        self.status = 0 # Status: 0: Nicht begonne, 1: Steht bereit für Deals, 2: Wird angefahren 3: Abgeschlossen
        self.initiator = None # Initiator der für job zuständig ist


