from random import randint
from time import process_time

# State baseclass
State = type("State", (object,), {})


# All the FSM classes
class Start(State):
    def execute(self):
        print("The washing Machine is idle and ready to clean")


class Cleaning(State):
    def execute(self):
        print("The washing Machine is currently in the cleaning cycle")


class Drying(State):
    def execute(self):
        print("The washing Machine is currently in the drying cycle")


# Allows the FSM to transition to a different state (Takes string)
class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def execute(self):
        print("Transitioning")


# the FSM itself
class FiniteStateMachine(object):
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None

    def SetState(self, stateName):
        # Reads the state in the state dict above
        self.curState = self.states[stateName]

    def Transition(self, transName):
        # Reads the transition in the transition dict above
        self.trans = self.transitions[transName]

    def execute(self):
        # Checks if there is a transition, if so it executes said transition and sets the current state to what the
        # transition is to, and lastly it resets the transition
        if self.trans:
            self.trans.execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.curState.execute()


# Creates an instant of the FSM
class Char(object):
    def __init__(self):
        self.FSM = FiniteStateMachine(self)
        self.Start = True
