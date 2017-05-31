from job import Job
from math import inf

# Speichert die Deals der einzelnen Agenten für die Initiatoren ab
class Deal(object):
    def __init__(self, agent, job):
        self.agent = agent # zugehöriger Agent
        self.job = job # Job für den der Deal ist
        self.bid = inf # Eingegebenes Angebot
        self.status_initiator = 0 # Status aus sich des Initiators
        self.pre_bid = 1 # Status aus sich des Agenten als Boolean
        job.initiator.deals.append(self)  # Der liste des Initiators hinzufügen


    # Ausgabe und eingabe für den Status aus sicht des Initiators
    def is_definitive_rejected(self):
        return 1 if self.status_initiator == 0 else 0

    def is_pre_rejected(self):
        return 1 if self.status_initiator == 1 else 0

    def is_pre_accepted(self):
        return 1 if self.status_initiator == 2 else 0

    def is_definitive_accepted(self):
        return 1 if self.status_initiator == 3 else 0

    def set_definitive_reject(self):
        self.status_initiator = 0

    def set_pre_reject(self):
        self.status_initiator = 1

    def set_pre_accept(self):
        self.status_initiator = 2

    def set_definitive_accept(self):
        self.status_initiator = 3


