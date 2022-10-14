import os



INPUT_FILE = "./input/280000_parole_italiane.txt"
FIRST = "./list/lista_"
THIRD = "_wordle_ita.txt"



def main():
    create_files()

    writes()

    start()


"""

create_files():         create the files .txt of each lenght of words from 4 to 9
return: 

"""

def create_files():
    for c in range(4, 10):
        NAME_OUTPUT = FIRST + str(c) + THIRD
        OUTPUT = open(NAME_OUTPUT, "w+")
        OUTPUT.close()


"""

write_on_files():       writes on the respective file for the corresponding index
argument:               int; c the length of the word
                        string; name the name of the file
return:

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
return: 

"""

def writes():
    for c in range(4, 10):
        NAME_OUTPUT = FIRST + str(c) + THIRD
        write_on_file(c, NAME_OUTPUT)


"""

start():                create the first word for the algorithm with all the checks necessary
argument:               set; SET_OF_WORD take the set containing all the 5 chars words
                        int; LIST_WORDS who represent the length of the word
                        list; the list of the words used
return:                 string; the first word of wordle

"""

def create_first_word(SET_OF_WORD, LIST_WORDS, WORD_USED):
    if len(WORD_USED) < 1: 
        MY_WORD = input("Inserisci una parola esistente da " + str(LIST_WORDS) + " caratteri:\n")
    else:
        MY_WORD = input("Inserisci una parola DELLA LISTA da " + str(LIST_WORDS) + " caratteri:\n")

    MY_WORD = MY_WORD.lower()

    while len(MY_WORD) != int(LIST_WORDS) or not MY_WORD.isalpha() or MY_WORD not in SET_OF_WORD:
        MY_WORD = ""
        if len(WORD_USED) < 1:
            MY_WORD = input("DEVI inserire una parola esistente da " + str(LIST_WORDS) + " caratteri:\n")
        else:
            MY_WORD = input("DEVI inserire una parola della lista da " + str(LIST_WORDS) + " caratteri:\n")

        MY_WORD = MY_WORD.lower()

    print("\n")
    return MY_WORD


"""

create_map():           create the map of all 1 for the confronting of the words
argument:               int; LIST_WORDS who represent the length of the word
return:                 list of dict of dict; the structure for keep in memory the state of the words

"""

def create_map(LIST_WORDS):
    HASHMAP = {}

    for i in range(0, 26):
        HASHMAP[i] = {}
        for j in range(0, int(LIST_WORDS)):
            HASHMAP[i][j] = 1

    return HASHMAP


"""

create_string_3value(): create a string of 0, 1 or 2 to represent the letter which could, has or can't be in the word
argument:               int; LIST_WORDS who represent the length of the word
return:                 string; the value of the string wiht 0, 1 or 2

"""

def create_string_3value(LIST_WORDS):
    MY_WORD = input("Scrivi una stringa lunga " + str(LIST_WORDS) + " cosi formata:\n\t0 se la lettera nella corrispettiva posizione NON esiste\n\t1 se la lettera nella corrispettiva posizione ESISTE ma NON e' in quella posizione\n\t2 se la lettera nella corrispettiva posizione ESISTE ed e' in posizione CORRETTA\n")
    ALLOWED = "012"

    while len(str(MY_WORD)) != int(LIST_WORDS) or not str(MY_WORD).isdecimal() or not all(ch in ALLOWED for ch in MY_WORD):
        MY_WORD = str("")
        MY_WORD = input("ERRORE!\nScrivi una stringa lunga " + str(LIST_WORDS) + " cosi formata:\n\t0 se la lettera nella corrispettiva posizione NON esiste\n\t1 se la lettera nella corrispettiva posizione ESISTE ma NON e' in quella posizione\n\t2 se la lettera nella corrispettiva posizione ESISTE ed e' in posizione CORRETTA\n")
    
    print("\n")
    return MY_WORD


"""

resolve():              try to resolve the words cycling until the input contains only 1 word
argument:               map; WORDS the map of all the possible Words
                        int; LIST_WORDS who represent the length of the word
return:                 

"""

def resolve(WORDS, LIST_WORDS):

    STRING_INDEX = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    MATRIX = create_map(LIST_WORDS)
    CHAR_ONE = []
    
    WORD_USED=[]

    while len(WORDS) > 1:
        WORD = create_first_word(WORDS, LIST_WORDS, WORD_USED)
        STRING_COMPARE = create_string_3value(LIST_WORDS)
        WORD_USED.append(WORD)
        
        for i in range(0, int(LIST_WORDS)):
            NUMBER = (STRING_INDEX[WORD[i]])
            """
            first check is when user insert the number 2 for a char: sets the corrisponding index of letter in MATRIX to 2 and  sets all
            the remain letters index to 0
            """

            if STRING_COMPARE[i] == str(2):
                MATRIX[NUMBER][i] = 2
                for j in range(0, 26):
                    if NUMBER != j:
                        MATRIX[j][i] = 0
                if WORD[i] in CHAR_ONE:
                    CHAR_ONE.remove(WORD[i])
            

            """
            second check is when user insert the number 0 for a char: set all the indexes of the letter equal to 0
            """

            if STRING_COMPARE[i] == str(0):
                for i in range(0, int(LIST_WORDS)):
                    if MATRIX[NUMBER][i] != 2:
                        MATRIX[NUMBER][i] = 0

            """
            third check is when user insert the number 1 for a char: set the corrispondig index to 0 and add it to the list of needed chars
            """

            if STRING_COMPARE[i] == str(1):
                if WORD[i] not in CHAR_ONE:
                    CHAR_ONE.append(WORD[i])
                MATRIX[NUMBER][i] = 0

        """
        confront the words in my set with my MATRIX to filter out the words we dont need
        """
        for word in WORDS.copy():
            for c in range(0, int(LIST_WORDS)):
                NUMBER = STRING_INDEX[word[c]]
                if MATRIX[NUMBER][c] == 0:
                    WORDS.remove(word)
                    break

        """
        remove the words that doesn't contain the letter needed
        """
        for word in WORDS.copy(): 
            for w in CHAR_ONE:
                if w not in word:
                    WORDS.remove(word)
                    break

        os.system('clear')
        print_list_words(WORD_USED)

        if len(WORDS) == 1:
            print("Congratulazioni! la parola e': " + WORDS.pop())
        elif len(WORDS) > 1:
            print("Lista di possibili parole:")
            print_set(WORDS)
            optimize(WORDS, LIST_WORDS)
        else:
            print("Qualcosa e' andato storto, non e' stata trovata alcuna parola :(")


"""

optimize:               try to optimize the word to select
argument:               set; WORDS the set of the possible words
                        string; LIST_WORDS is the length of word
return:

"""

def optimize(WORDS, LIST_WORDS):
    """
    Step 1: create a map which count the frequency of the letters that appear in each word and sort it in descending order
    """

    LETTER_COUNT = {}
    for word in WORDS:
        for c in word:
            if c in LETTER_COUNT:
                LETTER_COUNT[c] = LETTER_COUNT[c] + 1
            else:
                LETTER_COUNT[c] = 1

    LETTER_COUNT = dict(sorted(LETTER_COUNT.items(), key=lambda item: item[1], reverse=True))

    """
    Step2: create the map which contain the score of each word based on letters in and the score of the letter
    """

    WORD_COUNT = {}
    for word in WORDS:
        CONTAINS = []
        TOTAL = 0
        for c in word:
            if c not in CONTAINS:
                TOTAL = TOTAL + LETTER_COUNT[c]
                CONTAINS.append(c)

        WORD_COUNT[word] = TOTAL

    WORD_COUNT = dict(sorted(WORD_COUNT.items(), key=lambda item: item[1], reverse=True))

    """
    Step3: create the list with the best possible words for given input
    """

    print("Lista migliori parole: ")

    if len(WORD_COUNT) > int(LIST_WORDS):
        LIMIT = int(LIST_WORDS) - 1
        for key in WORD_COUNT:
            print(key + ' --> ' + str(WORD_COUNT[key]))
            LIMIT = LIMIT - 1
            if LIMIT < 0:
                break
    else:
        for key in WORD_COUNT:
            print(key + ' --> ' + str(WORD_COUNT[key]))

    print('\n\n')
    



"""

print_list_words():     print the list of words used
argument:               list; WORD_USED is the list passed of all word used from the user
return:

"""

def print_list_words(WORD_USED):
    i = 0
    print("Lista di parole usate:")
    for w in WORD_USED:
        if i < len(WORD_USED) - 1:
            print(w, end=', ')
        else:
            print(w + "\n\n\n")
        i = i + 1


"""

print_set():            print the set in the argument
argument:               set; the set we wanna print
return:


"""

def print_set(SET):
    i = 0
    for w in SET:
        if i < len(SET) - 1:
            print(w, end='\t')
        else:
            print(w + "\n\n\n")
        i = i + 1


"""

start():                start the algorithm and let the user choice how long is the word to guess
return:

"""

def start():
    LIST_WORDS = input("Inserisci la lunghezza della parola da indovinare: ")
    ALLOW = "456789"
    while len(str(LIST_WORDS)) != 1 or not str(LIST_WORDS).isdecimal() or not all(ch in ALLOW for ch in LIST_WORDS):
        LIST_WORDS = ""
        LIST_WORDS = input("Inserisci la lunghezza della parola da indovinare: ")

    LIST_WORDS_ALL = "./list/lista_" + str(LIST_WORDS) + "_wordle_ita.txt"
    INPUT = open(LIST_WORDS_ALL, "r")
    WORDS = set()

    for word in INPUT:
        WORDS.add(word.strip())

    INPUT.close()
    resolve(WORDS, LIST_WORDS)


if __name__ == "__main__":
    main()
