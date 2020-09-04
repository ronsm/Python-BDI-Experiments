import colorama
from colorama import Fore, Style
import threading
import time
import requests

class ros_bridge_client(object):
    def __init__(self, belief_manager):
        self.agent_id = 'ros_bridge_client'
        self.log('init')

        self.belief_manager = belief_manager

        self.ros_server_url = 'http://192.168.175.141:8888/'

    def send(self, agent, service, args, result_recipient):
        url = self.ros_server_url + 'service_request'

        agent = str(agent)
        service = str(service)
        args = str(args)
    
        form = {
            'agent' : agent,
            'service' : service,
            'args' : args
        }
        r = requests.post(url, data=form)
        response = r.text
        self.log(response)

        t = threading.Thread(target =  self.spawn_watchdog, args = (service, response, result_recipient))
        t.start()

    def spawn_watchdog(self, service, response, result_recipient):
        url = self.ros_server_url + 'service_request_status'
        form = {
            'client_id' : response
        }

        status = -1
        while(status == -1):
            log_msg = 'waiting on a response to service request: ' + response + ' for agent: ' + result_recipient
            self.log(log_msg)

            r = requests.post(url, data=form)
            r = r.text
            status = int(r)

            time.sleep(2)
            
        log_msg = 'response received for service request: ' + response + ' for agent: ' + result_recipient + ', response = ' + str(status)
        self.log(log_msg)

        self.belief_manager.send_to_agent(result_recipient, service, status, self.agent_id)

    def log(self, msg):
        tag = '[' + self.agent_id + ']'
        print(Fore.CYAN + tag, Fore.RESET + msg)