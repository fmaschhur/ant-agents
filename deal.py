from job import Job


class Deal(object):
    def __init__(self, agent, time, job):
        self.agent = agent
        self.job = job
        self.time = time
        self.status_initiator = 0
        self.pre_bid = 1

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


