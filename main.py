from world import World
import graph
from logger import Logger
import tkinter as tk
import time


class Main:

    params_file = 'params.txt'
    params = {}
    ant_world = None
    tk_root = tk.Tk()

    interval = 0.5
    scale = 100

    @staticmethod
    def run():
        Main.read_params()
        ant_world = World(Main.params)
        ant_world.graph = graph.Graph(Main.params_file)
        ant_world.populate()

        ant_world_logger = Logger(ant_world, Main.tk_root, Main.scale)
        # ant_world_logger.get_curr_state()
        # ant_world_logger.print_curr_state()
        #
        # ant_world_logger.draw_curr_state()

        for i in range(Main.params['loops']):
            ant_world_logger.get_curr_state()
            ant_world_logger.print_curr_state()

            ant_world_logger.draw_curr_state()
            #Main.tk_root.after(Main.interval, ant_world_logger.draw_curr_state(Main.tk_root, Main.scale))

            Main.tk_root.update_idletasks()
            Main.tk_root.update()
            time.sleep(Main.interval)

            ant_world.simulate_cycle()

        tk.mainloop()

    @staticmethod
    def read_params():
        file_obj = open(Main.params_file)
        for line in file_obj:
            name = line.partition(": ")[0]
            value = int(line.split(": ")[1])
            Main.params[name] = value


if __name__ == "__main__":
    Main.run()