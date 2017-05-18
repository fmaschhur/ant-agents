from world import World
import graph
from logger import Logger


class Main:

    ant_world = None

    @staticmethod
    def run():
        # self.file = params_file
        ant_world = World()
        ant_world.graph = graph.Graph(ant_world.file)
        ant_world_logger = Logger(ant_world)
        ant_world.populate()

        for i in range(ant_world.params("loops")):
            ant_world.simulate_cycle()
            ant_world_logger.get_state()
            ant_world_logger.print_state()


if __name__ == "__main__":
    Main.run()