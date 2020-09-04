from os import listdir
from os.path import isfile, join
import importlib
from service_manager import service_manager
from belief_manager import belief_manager
from ros_bridge_client import ros_bridge_client
import colorama
from colorama import Fore, Style

class super(object):
    def __init__(self):
        self.agent_id = 'super'
        self.startup_msg()
        self.log('init')

        self.service_manager = service_manager()
        self.belief_manager = belief_manager()
        self.ros_bridge_client = ros_bridge_client(self.belief_manager)

        self.agent_instances = {}

        agent_files = [f for f in listdir('agents') if isfile(join('agents', f))]
        
        agent_class_names = []
        for agent in agent_files:
            agent_class_name = agent.split(".")[0]
            agent_class_names.append(agent_class_name)

        for agent_class_name in agent_class_names:
            path = 'agents.' + agent_class_name
            module = importlib.import_module(path)
            agent_class = getattr(module, agent_class_name)
            agent_instance = agent_class(self.service_manager, self.belief_manager, self.ros_bridge_client)

            self.agent_instances[agent_class_name] = agent_instance
            self.belief_manager.enrol_agent(agent_class_name)

        self.service_manager.register_agent_instances(self.agent_instances)

        # scenarto testing
        self.belief_manager.send_to_all('user', 'bob', self.agent_id)

        self.belief_manager.send_to_all('doorbell_pressed', 'true', self.agent_id)

        for agent in self.agent_instances.values():
            agent.run()
    
    def log(self, msg):
        tag = '[' + self.agent_id + ']'
        print(Fore.CYAN + tag, Fore.RESET + msg)

    def startup_msg(self):
        print(Fore.YELLOW + '* * * * * * * * * * * * * * * * * *')
        print()
        print(Style.BRIGHT + ' Untitled Project' + Style.RESET_ALL + Fore.YELLOW)
        print()
        print(' Developer: Ronnie Smith')
        print(' Email:     ronnie.smith@ed.ac.uk')
        print(' GitHub:    @ronsm')
        print()
        print('* * * * * * * * * * * * * * * * * *')

if __name__ == "__main__":
    super_instance = super()