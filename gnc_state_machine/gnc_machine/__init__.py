
class State:
    """ 
    This class defines a state in a finite state machine. 
    
    potential_states: List of state instances that this state is allowed to transition to
    fail_state: A state object that this class will transition to in the event of an error

    """
    def __init__(self, potential_states:list, fail_state):
        """ Sets up a state object """
        self.potential_states = potential_states
        self.fail_state = fail_state


class GNCMachine:
    """ 
    This class will model a finite state machine 

    The machine's configuration will be yaml-configured. 
    """

    def __init__(self):
        """ Instantiate the finite state machine """
        self.startState = None

