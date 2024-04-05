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
    
    def create_diag_without_letter(letter):
        stateDiagram = [
                 #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z     
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #state 0
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #trap state

        ]
        
        letter_index = ord(letter) - ord('a')
        stateDiagram[0][letter_index] = 1
        
        return stateDiagram


        #example: no 'a'
        # stateDiagram = [
        #          #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z     
        #          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #state 0
        #          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #trap state

        # ]
        # acceptingState = 0
    