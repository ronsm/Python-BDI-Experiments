import pprint
import colorama
from colorama import Fore, Style

class belief_manager(object):
    def __init__(self):
        self.agent_id = 'belief_manager'
        self.log('init')

        self.all_agent_beliefs = {}

    def enrol_agent(self, agent):
        agent_beliefs = []
        self.all_agent_beliefs[agent] = agent_beliefs
        log_msg = 'agent enrolled: ' + agent
        self.log(log_msg)

    def get_belief_value(self, agent, belief_name):
        agent_beliefs = self.all_agent_beliefs.get(agent)
        for belief in agent_beliefs:
            if belief[0] == belief_name:
                return belief[1]

        log_msg = "belief not found, agent: " + agent + " belief: " + belief_name
        self.log(log_msg)
        return False

    def send_to_agent(self, agents, belief_name, belief_value, source):
        belief_tuple = (belief_name, belief_value, source)
        if isinstance(agents, list):
            for agent in agents:
                agent_beliefs = self.all_agent_beliefs.get(agent)
                agent_beliefs.append(belief_tuple)
                self.all_agent_beliefs[agent] = agent_beliefs
        else:
                agent = agents
                agent_beliefs = self.all_agent_beliefs.get(agent)
                agent_beliefs.append(belief_tuple)
                self.all_agent_beliefs[agent] = agent_beliefs

    def delete_from_agent(self, agents, belief_name, belief_value, source):
        if isinstance(agents, list):
            for agent in agents:
                agent_beliefs = self.all_agent_beliefs.get(agent)
                for belief in agent_beliefs:
                    if belief[0] == belief_name and belief[1] == belief_value:
                        del agent_beliefs[agent_beliefs.index(belief)]
        else:
            agent = agents
            agent_beliefs = self.all_agent_beliefs.get(agent)
            for belief in agent_beliefs:
                if belief[0] == belief_name and belief[1] == belief_value:
                    del agent_beliefs[agent_beliefs.index(belief)]

    def update_to_agent(self, agents, belief_name, belief_value, source):
        if isinstance(agents, list):
            for agent in agents:
                old_belief_value = self.get_belief_value(agent, belief_name)
                self.delete_from_agent(agent, belief_name, old_belief_value, source)
                self.send_to_agent(agent, belief_name, belief_value, source)
        else:
            agent = agents
            old_belief_value = self.get_belief_value(agent, belief_name)
            self.delete_from_agent(agent, belief_name, old_belief_value, source)
            self.send_to_agent(agent, belief_name, belief_value, source)

    def send_to_all(self, belief_name, belief_value, source):
        belief_tuple = (belief_name, belief_value, source)
        for key in self.all_agent_beliefs.keys():
            agent_beliefs = self.all_agent_beliefs.get(key)
            agent_beliefs.append(belief_tuple)
            self.all_agent_beliefs[key] = agent_beliefs

    def delete_from_all(self, belief_name, belief_value, source):
        for key in self.all_agent_beliefs.keys():
            agent_beliefs = self.all_agent_beliefs.get(key)
            for belief in agent_beliefs:
                if belief[0] == belief_name and belief[1] == belief_value:
                    del agent_beliefs[agent_beliefs.index(belief)]

    def print_all_agent_beliefs(self):
        pprint.pprint(self.all_agent_beliefs)

    def log(self, msg):
        tag = '[' + self.agent_id + ']'
        print(Fore.CYAN + tag, Fore.RESET + msg)