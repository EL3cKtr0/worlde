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

create_matrix():        create the matrix of all 0 for the confronting of the words
return:                 2D Array; the matrix

"""

def create_matrix():
    a = []
    b = []
    for i in range(0, 5):
        b.append(1)
    for j in range(0, 26):
        a.append(b)
    return a



"""

create_string_3value(): create a string of 0, 1 or 2 to represent the letter which could, has or can't be in the word
return:                 string; the value of the string wiht 0, 1 or 2

"""

def create_string_3value():
    MY_WORD = input("\nScrivi una stringa lunga 5 cosi formata:\n\t0 se la lettera nella corrispettiva posizione NON esiste\n\t1 se la lettera nella corrispettiva posizione ESISTE ma NON e' in quella posizione\n\t2 se la lettera nella corrispettiva posizione ESISTE ed e' in posizione CORRETTA\n")
    ALLOWED = "012"

    while len(str(MY_WORD)) != 5 or not str(MY_WORD).isdecimal() or not all(ch in ALLOWED for ch in MY_WORD):
        MY_WORD = str("")
        MY_WORD = input("\nERRORE!\nScrivi una stringa lunga 5 cosi formata:\n\t0 se la lettera nella corrispettiva posizione NON esiste\n\t1 se la lettera nella corrispettiva posizione ESISTE ma NON e' in quella posizione\n\t2 se la lettera nella corrispettiva posizione ESISTE ed e' in posizione CORRETTA\n")

    return MY_WORD



"""

resolve():              try to resolve the words cycling until the input contains only 1 word
argument:               set; the set of all the possible Words
return:                 

"""

def resolve(WORDS):
    while len(WORDS) > 1:
        WORD = create_first_word(WORDS)
        MATRIX = create_matrix()
        STRING_COMPARE = create_string_3value()




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

    INPUT.close()
    resolve(WORDS)




print("Generating files..")
create_files()

print("Writing on files..")
writes()


start()
