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
        print("The washing machine is currently in the cleaning cycle")


class Drying(State):
    def execute(self):
        print("The washing machine is currently in the drying cycle")


class Finished(State):
    def execute(self):
        print("The washing machine is finished")


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


if __name__ == "__main__":
    washingMachine = Char()

    washingMachine.FSM.states["Start"] = Start()
    washingMachine.FSM.states["Clean"] = Cleaning()
    washingMachine.FSM.states["Dry"] = Drying()
    washingMachine.FSM.states["Fin"] = Finished()
    washingMachine.FSM.transitions["toWash"] = Transition("Clean")
    washingMachine.FSM.transitions["toDry"] = Transition("Dry")
    washingMachine.FSM.transitions["Finish"] = Transition("Fin")

    washingMachine.FSM.setState("Start")

    for i in range(20):
        startTime = time.time()
        timeInterval = 1

        while startTime + timeInterval > time.time():
            pass

        if randint(0, 3):
            if washingMachine.Start:
                washingMachine.FSM.Transition("toDry")
                washingMachine.Start = False

            elif washingMachine.Cleaning:
                washingMachine.FSM.Transition("toDry")
                washingMachine.Cleaning = False

            elif washingMachine.Drying:
                washingMachine.FSM.Transition("Done")
                washingMachine.Drying = False

        washingMachine.FSM.execute()

