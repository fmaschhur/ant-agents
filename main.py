from world import World
import graph
from logger import Logger


class Main:

    params_file = 'params.txt'
    params = {}
    ant_world = None

    @staticmethod
    def run():
        Main.read_params()
        ant_world = World(Main.params)
        ant_world.graph = graph.Graph(Main.params_file)
        ant_world_logger = Logger(ant_world)
        ant_world.populate()

        ant_world_logger.get_state()
        ant_world_logger.print_state()
        for i in range(Main.params['loops']):
            ant_world.simulate_cycle()
            ant_world_logger.get_state()
            ant_world_logger.print_state()

    @staticmethod
    def read_params():
        file_obj = open(Main.params_file)
        for line in file_obj:
            name = line.partition(": ")[0]
            value = int(line.split(": ")[1])
            Main.params[name] = value


if __name__ == "__main__":
    Main.run()