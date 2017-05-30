from graph import Graph
from agent import Agent
from initiator import Initiator
from job import Job


class World(object):

    def __init__(self, params):
        self.agents = []
        self.agents_data = params['agents_data'] # preferences der agenten und so #TODO
        self.agents_init = params['agents_init']
        self.graph = Graph(params)
        self.wait = params['wait']
        self.jobs = jobs(params['jobs']) # TODO wie lesen wir ein array ein?
        self.initiators = []
        self.time = 0

    def jobs(self, job_params):
    # TODO; erstellt jobs mit übergebenen parametern

    def populate(self):
        for i in range(self.agents_init):
            agent = Agent(i, position, 20, 3, [5, 6, 7, 1, 2], 2)
            self.agents.append(agent)

    def simulate_cycle(self):
        new_jobs = []

        for job in self.jobs:
            if job.time == self.time:
                job.status = 1
                init = Initiator(job)
                self.initiators.append(init)
                new_jobs.append(init)

        for agent in self.agents:
            agent.new_deals(new_jobs)

        for initiator in self.initiators:
            if initiator.answer():
                self.initiators.remove(initiator)

        for agent in self.agents:
            agent.move()
