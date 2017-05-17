import world
import graph
import logger


class Main:

    ant_world = None

    @staticmethod
    def run():
        # self.file = params_file
        ant_world = world.World()
        ant_world.graph = graph.Graph(ant_world.file)
        ant_world_logger = logger.Logger(ant_world)
        ant_world.populate()

        for i in range(ant_world.params("loops")):
            ant_world.simulate_cycle()
            ant_world_logger.get_state()
            ant_world_logger.print_state()


if __name__ == "__main__":
    Main.run()