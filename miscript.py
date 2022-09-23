INPUT_FILE = "./input/660000_parole_italiane.txt"
FIRST = "./list/lista_"
THIRD = "_wordle_ita.txt"

"""

create_files():         create the files .txt of each lenght of words from 4 to 9
return:                 null;

"""
def create_files():
    for c in range(4, 10):
        NAME_OUTPUT = FIRST + str(c) + THIRD
        OUTPUT = open(NAME_OUTPUT, "w")
        OUTPUT.close()

"""

write_on_files():       writes on the respective file for the corresponding index
return:                 null;

"""
def write_on_file(c, name):
    INPUT = open(INPUT_FILE, "r")
    OUT = open(name, "w")
    for word in INPUT:
        if len(word) == c + 1:
            OUT.write(word)
    INPUT.close()
    OUT.close()

"""

writes():               for each file from 4 to 9 call the write_on_files function
return:                 null;

"""
def writes():
    for c in range(4, 10):
        NAME_OUTPUT = FIRST + str(c) + THIRD
        write_on_file(c, NAME_OUTPUT)


"""

start():                create the first word for the algorithm with all the checks necessary
argument:               set; take the set containing all the 5 chars words 
return:                 string; the first word of wordle

"""

def create_first_word(SET_OF_WORD):
    MY_WORD = input("Inserisci una parola esistente da 5 caratteri:\n")
    MY_WORD = MY_WORD.lower()

    while len(MY_WORD) != 5 or not MY_WORD.isalpha() or MY_WORD not in SET_OF_WORD:
        MY_WORD = ""
        MY_WORD = input("DEVI inserire una parola esistente da 5 caratteri:\n")
        MY_WORD = MY_WORD.lower()

    return MY_WORD


"""

start():                start the algorithm
return:                 null;

"""
def start():
    LIST_WORDS_5 = "./list/lista_5_wordle_ita.txt"
    INPUT = open(LIST_WORDS_5, "r")
    WORDS = set()

    for word in INPUT:
        WORDS.add(word.strip())

    FIRST_WORD = create_first_word(WORDS)

    NEDDED_CHARS = set()
    POSSIBLE_CHARS = set()




print("Generating files..")
create_files()

print("Writing on files..")
writes()

print("Creating data list with all words")
start()
