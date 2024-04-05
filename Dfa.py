class Dfa:
    state_diagram = None
    accepting_state = -1
    
    def __init__(self, stateDiagram, acceptingState):
        self.state_diagram = stateDiagram
        self.accepting_state = acceptingState
    
    def get_state_diagram(self):
        return self.state_diagram
    
    def get_accepting_state(self):
        return self.accepting_state
    
    def is_string_accepted(self, inputString):
        startState = 0
        #acceptingState = 1 #TODO: make a class to encapsulate the state diagram transitions and the accepting state(s)

        while inputString:
            currentState = startState
    
            for char in inputString:
                integer_value = ord(char) - ord('a')
                #print(integer_value, char)
                currentState = self.state_diagram[currentState][integer_value]
           
    
            if currentState == self.accepting_state:
                return True
            else:
                return False
        return False
    