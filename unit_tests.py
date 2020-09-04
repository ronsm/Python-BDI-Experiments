# service call with wait
self.belief_manager.print_all_agent_beliefs()
instance = self.service_manager.search_service('human_position_estimate')
instance.service_request('human_position_estimate', ['personA'], self.agent_id)
self.belief_manager.print_all_agent_beliefs()
belief_value = self.wait_for_belief('user_location')
self.belief_manager.print_all_agent_beliefs()

# belief manager test
self.belief_manager.send_to_agent(['facial_recognition_service', 'home_automation_agent'], 'doorbell_pressed', 'true', self.agent_id)
self.belief_manager.print_all_agent_beliefs()
self.belief_manager.delete_from_agent(['facial_recognition_service', 'home_automation_agent'], 'doorbell_pressed', 'true', self.agent_id)
self.belief_manager.print_all_agent_beliefs()
self.belief_manager.send_to_all('toast_ready', 'false', self.agent_id)
self.belief_manager.print_all_agent_beliefs()
self.belief_manager.update_to_agent('facial_recognition_service', 'toast_ready', 'true', self.agent_id)
self.belief_manager.print_all_agent_beliefs()
self.belief_manager.delete_from_all('toast_ready', 'false', self.agent_id)
self.belief_manager.print_all_agent_beliefs()