import pprint
import colorama
from colorama import Fore, Style

class service_manager(object):
    def __init__(self):
        self.agent_id = 'service_manager'
        self.log('init')

        self.service_catalogue = {}
        self.agent_instances = {}

    def enrol_agent(self, agent):
        agent_arr = []
        self.service_catalogue[agent] = agent_arr
        log_msg = 'agent enrolled: ' + agent
        self.log(log_msg)

    def register_agent_instances(self, agent_instances):
        self.agent_instances = agent_instances
        log_msg = 'registered agent instances'
        self.log(log_msg)

    def register_service(self, agent, service):
        agent_arr = self.service_catalogue.get(agent)
        agent_arr.append(service)
        self.service_catalogue[agent] = agent_arr
        log_msg = 'service enrolled: ' + service + ' for agent: ' + agent
        self.log(log_msg)

    def search_service(self, service):
        for key, values in self.service_catalogue.items():
            for value in values:
                if value == service:
                    # log_msg = 'found: ' + service
                    # self.log(log_msg)
                    return self.agent_instances[key]

    def print_service_catalogue(self):
        pprint.pprint(self.service_catalogue)

    def log(self, msg):
        tag = '[' + self.agent_id + ']'
        print(Fore.CYAN + tag, Fore.RESET + msg)