from graph import Graph
from agent import Agent
from position import Position
from initiator import Initiator
from job import Job


class World(object):

    def __init__(self, params):
        self.agents = []
        self.agents_data = params['agents_data'] # preferences der agenten und so #TODO
        self.agents_init = params['agents_init']
        self.graph = Graph(params)
        self.wait = params['wait']
        self.jobs = []
        self.create_jobs(params['jobs']) # TODO wie lesen wir ein array ein?
        self.initiators = []
        self.time = 0

    def create_jobs(self, job_params):
        for i in range(0, 10):
                job = Job(i, i * 100, self.graph.random_node())
                self.jobs.append(job)
        # TODO; erstellt jobs mit übergebenen parametern

    def populate(self):
        for i in range(self.agents_init):
            agent = Agent(i, self.graph.random_node(), 20, 3, [5, 6, 7, 1, 2], 2) # TODO präferenzen
            self.agents.append(agent)

    def simulate_cycle(self):
        new_jobs = []

        for job in self.jobs:
            if job.time == self.time:
                job.status = 1
                init = Initiator(job)
                job.initiator = init
                self.initiators.append(init)
                new_jobs.append(init)
        for agent in self.agents:
            agent.new_deals(new_jobs)

        for initiator in self.initiators:
            if initiator.answer():
                self.initiators.remove(initiator)

        for agent in self.agents:
            agent.move(self.graph)
