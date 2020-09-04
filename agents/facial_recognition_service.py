import colorama
from colorama import Fore, Style
import threading
import time

class facial_recognition_service(object):
    def __init__(self, service_manager, belief_manager):
        """
        IMPORTANT: Configuration

        You must add/edit:
            - Edit agent identifier to match the name of the agent class
            - Add a trigger sets to the trigger set dictionary for each plan
            - If the agent provides services, you must enrol them here
        """

        # the agent identifier
        self.agent_id = 'facial_recognition_service'
        self.log('init')

        self.service_manager = service_manager
        self.service_manager.enrol_agent(self.agent_id)

        self.belief_manager = belief_manager

        self.trigger_sets = {}

        # register services here
        self.service_manager.register_service(self.agent_id, 'recognise_face')
        
        # add trigger sets to the dictionary here
        # none

    """ Core Agent Functions """
    """     DO NOT EDIT      """

    def run(self):
        log_msg = "running"
        self.log(log_msg)

        t = threading.Thread(target =  self.trigger_set_monitor)
        t.start()

    # WARNING: This only handles single belief triggers!
    # TODO: Add capability to check multiple tuples in a list.
    def trigger_set_monitor(self):
        while(1):
            for key, value in self.trigger_sets.items():
                belief_value = self.belief_manager.get_belief_value(self.agent_id, value[0])
                if belief_value == value[1]:
                    self.belief_manager.delete_from_agent(self.agent_id, value[0], value[1], self.agent_id)
                    self.trigger_plan(key)
            time.sleep(1)

    def trigger_plan(self, plan):
        method = getattr(self, plan)
        t = threading.Thread(target = method)
        t.start()

    def wait_for_belief(self, belief):
        while(1):
            belief_exists = self.belief_manager.get_belief_value(self.agent_id, belief)
            if not belief_exists:
                time.sleep(1)
                log_msg = "waiting..."
                self.log(log_msg)
            else:
                return belief_exists

    def service_request(self, service, args, result_recipient):
        method = getattr(self, service)
        t = threading.Thread(target =  method, args = (args, result_recipient))
        t.start()

    def log(self, msg):
        tag = '[' + self.agent_id + ']'
        print(Fore.CYAN + tag, Fore.RESET + msg)

    """ Agent Services """

    # service methods
    def recognise_face(self, args, result_recipient):
        image_URL = args[0]
        person = "james"
        time.sleep(2)
        self.belief_manager.send_to_agent(result_recipient, 'person_in_image', person, self.agent_id)

    """ Agent Plans """

    # plan methods
    # none