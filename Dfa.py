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
        
        letter_as_index = ord(letter) - ord('a')
        stateDiagram[0][letter_as_index] = 1
        
        #note: accepting state must be 0 in this dfa
        return stateDiagram
    
    #TODO: delete unneeded rows while creating this state diagram? (unused states are common)
    def create_diag_with_letter_index(letter, index):
        stateDiagram = [
              #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z         
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #state 0
              [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], #state 1
              [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], #state 2
              [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], #state 3
              [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], #state 4
              [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], #state 5 (perpetual accepting state)
              [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]  #state 6 (trap state)
        
        ]
        
        letter_as_index = ord(letter) - ord('a')
        
        #rows before the index stay the same
        #(each state simply leads to the next state)

        #first row after the index:
            #if it's the target letter, go to the accepting state
            #if it's not the target letter, go to the trap state

        for k in range(26):
            if k == letter_as_index:
                stateDiagram[index][k] = 5 #point to accepting state
            else:
                stateDiagram[index][k] = 6 #point to trap state
                
        #we only have to change one row
        #the rest of the rows (besides accepting and trap) represent states which cannot be accessed

        
        #note: accepting state must be 5 in this dfa
        return stateDiagram





 ############################################################################################################################
    #example DFA tables
    #need to create support for NFAs?

    #has an 'a'
    # stateDiagram = [
    #     #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z         
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #state 0
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #state 1
    # ]
    # acceptingState = 1

    #has an 'a' as a third character
    # stateDiagram = [
    #           #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z         
    #           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #state 0
    #           [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], #state 1
    #           [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], #state 2
    #           [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], #state 3 (perpetual accepting state)
    #           [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]  #state 4 (trap state)
        
    # ]
    # acceptingState = 3

    #DOES NOT have an 'a' as the third character
    #note: this is the same as the previous state diagram, but the 3's and 4's in state 2 are swapped
    # stateDiagram = [
    #            #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
    #            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #state 0
    #            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2, 2], #state 1
    #            [4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], #state 2
    #            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], #state 3 (perpetual accepting state)
    #            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]  #state 4 (trap state)
               

    # ]
    # acceptingState = 3



    #no 'a' at all
    # stateDiagram = [
    #              #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z     
    #              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #state 0
    #              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #trap state

    # ]
    # acceptingState = 0
    