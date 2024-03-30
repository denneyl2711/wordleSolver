WORD_SOURCE = "wordleAnswers.txt"

def load_dictionary():
    with open(WORD_SOURCE) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


#make sure to include nfa things
#scrabble solver things are on canvas


def main():
    wordle_answer_words = load_dictionary()
    for word in wordle_answer_words:
        print(word)
        
    #array of guesses
    #hard code the first two words ---> stair & bound
    #calculate better first two guesses later?
    guesses = ["stair", "bound", "", "", "", ""]
    

if __name__ == '__main__':
    main()