import time
from random import randint

# State baseclass
State = type("State", (object,), {})


# All the FSM classes
class Start(State):
    def execute(self):
        print("The washing machine is idle and ready to clean")


class Cleaning(State):
    def execute(self):
        print("The washing machine is currently running the cleaning cycle")


class Drying(State):
    def execute(self):
        print("The washing machine is currently running the drying cycle")


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

    def setState(self, stateName):
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
            self.setState(self.trans.toState)
            self.trans = None
        self.curState.execute()


# Creates an instant of the FSM
class Char(object):
    def __init__(self):
        self.FSM = FiniteStateMachine(self)
        self.Start = True
        self.Cleaning = True
        self.Drying = True
        self.Finished = True


if __name__ == "__main__":
    washingMachine = Char()

    washingMachine.FSM.states["Start"] = Start()
    washingMachine.FSM.states["Clean"] = Cleaning()
    washingMachine.FSM.states["Dry"] = Drying()
    washingMachine.FSM.transitions["toWash"] = Transition("Clean")
    washingMachine.FSM.transitions["toDry"] = Transition("Dry")

    washingMachine.FSM.setState("Start")

    for i in range(20):
        startTime = time.time()
        timeInterval = 1

        while startTime + timeInterval > time.time():
            pass

        fsmInput = input("Please select what cycle you would like to activate \n"
                         "1. Washing Cycle \n"
                         "2. Drying Cycle \n"
                         "3. Exit \n"
                         "Enter your choice ")

        match fsmInput:
            case "1":
                washingMachine.FSM.Transition("toWash")
                washingMachine.Start = False

            case "2":
                washingMachine.FSM.Transition("toDry")
                washingMachine.Start = False

            case "3":
                break

        washingMachine.FSM.execute()
