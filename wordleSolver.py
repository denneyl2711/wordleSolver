from re import L
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
    
    
    #test_dfa = Dfa(stateDiagram, acceptingState)
    diagram_without_letter = Dfa.create_diag_without_letter('l')
    test_dfa = Dfa(diagram_without_letter, 0)  # accepting state is 0 for diagrams which only check if a letter is present

    diagram_letter_index = Dfa.create_diag_with_letter_index('g', 3)
    test_dfa_2 = Dfa(diagram_letter_index, 5)

    #test_dfa_2 = Dfa(Dfa.create_diag_without_letter('a'), 0)
    
    intersection_dfa = Dfa.create_dfa_intersection(test_dfa, test_dfa_2)
    
    print(intersection_dfa)

    count = 0
    max_matches = 10
    for word in wordle_answer_words:
        #print(word + " is accepted: " + str(test_dfa.is_string_accepted(word)))

        # if (test_dfa_2.is_string_accepted(word)):
        #     print(word + " is accepted: " + str(test_dfa_2.is_string_accepted(word)))

        # if test_dfa.is_string_accepted(word) and test_dfa_2.is_string_accepted(word):
        #     print(word + " is accepted")

        if intersection_dfa.is_string_accepted(word):
            print(word + " is accepted")
           
            
            
        if test_dfa.is_string_accepted(word) and test_dfa_2.is_string_accepted(word):
            print("            " + word + " accepted by manual intersection")
            count = count + 1
            if count >= max_matches:
                break
    
    

if __name__ == '__main__':
    main()
    



