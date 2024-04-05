from turtle import write_docstringdict
from Dfa import Dfa


WORD_SOURCE = "wordleAnswers.txt"

def load_dictionary():
    with open(WORD_SOURCE) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


def main():
    wordle_answer_words = load_dictionary()
    # for word in wordle_answer_words:
    #     print(word)
        
    #array of guesses
    #hard code the first two words ---> stair & bound
    #calculate better first two guesses later?
    guesses = ["stair", "bound", "", "", "", ""]
    
    ###############################################
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
    stateDiagram = [
                 #a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z     
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #state 0
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  #trap state

    ]
    acceptingState = 0
    
    count = 0
    max_words = 10
    #test_dfa = Dfa(stateDiagram, acceptingState)
    diagram_without_letter = Dfa.create_diag_without_letter('l')
    test_dfa = Dfa(diagram_without_letter, 0) #accepting state is 0 for diagrams which only check if a letter is present
    
    for word in wordle_answer_words:
        print(word + " is accepted: " + str(test_dfa.is_string_accepted(word)))
        count = count + 1
        if count >= max_words:
            break;
    
    

if __name__ == '__main__':
    main()
    



