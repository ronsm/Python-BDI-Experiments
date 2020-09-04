import colorama
from colorama import Fore, Style
import threading
import time

class ros_bridge_client(object):
    def __init__(self, belief_manager):
        self.agent_id = 'ros_bridge_client'
        self.log('init')

        self.belief_manager = belief_manager

    def send(self, agent, service, args):
        print('test')

    def log(self, msg):
        tag = '[' + self.agent_id + ']'
        print(Fore.CYAN + tag, Fore.RESET + msg)