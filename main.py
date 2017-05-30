from world import World
from logger import Logger
import tkinter as tk
import time


class Main:

    params_file = 'params.txt'
    params = {}
    agent_world = None
    tk_root = tk.Tk()

    @staticmethod
    def run():
        Main.read_params()

        agent_world = World(Main.params)

        agent_world.populate()

        agent_world_logger = Logger(agent_world, Main.tk_root, Main.params['graphic_scale'])
        # agent_world_logger.get_curr_state()
        # agent_world_logger.print_curr_state()
        #
        # agent_world_logger.draw_curr_state()

        for i in range(Main.params['loops']):
            agent_world_logger.get_curr_state()
            agent_world_logger.print_curr_state()
            agent_world_logger.draw_curr_state()
            agent_world_logger.write_log()

            Main.tk_root.update_idletasks()
            Main.tk_root.update()
            time.sleep(Main.params['wait'])
            agent_world.simulate_cycle()

        tk.mainloop()
        agent_world_logger.file.close()

    @staticmethod
    def read_params():
        file_obj = open(Main.params_file)
        for line in file_obj:
            name = line.partition(": ")[0]
            value = int(line.split(": ")[1])
            Main.params[name] = value
        file_obj.close()


if __name__ == "__main__":
    Main.run()
