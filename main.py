#!/usr/bin/env python3

import os

def main():
    INPUT_FILE = "./input/280000_parole_italiane.txt"
    FIRST = "./list/lista_"
    THIRD = "_wordle_ita.txt"

    create_files(FIRST, THIRD)

    writes(INPUT_FILE, FIRST, THIRD)

    start()


"""

create_files():         create the files .txt of each lenght of words from 4 to 9
return: 

"""

def create_files(FIRST, THIRD):
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

def write_on_file(INPUT_FILE, c, name):
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

def writes(FILE, FIRST, THIRD):
    for c in range(4, 10):
        NAME_OUTPUT = FIRST + str(c) + THIRD
        write_on_file(FILE, c, NAME_OUTPUT)


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
    
    print('\n')
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

    print('\n')
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
    
    WORD_USED = []
    STRING_COMPARE_USED = []

    while len(WORDS) > 1:
        WORD = create_first_word(WORDS, LIST_WORDS, WORD_USED)
        WORD_USED.append(WORD)
        STRING_COMPARE = create_string_3value(LIST_WORDS)
        STRING_COMPARE_USED.append(STRING_COMPARE)
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

        """
        printing everything and optimize the choice
        """

        os.system('clear')
        print_list_words(WORD_USED, STRING_COMPARE_USED)

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
    Step1: create a map which count the frequency of the letters that appear in each word and sort it in descending order
    """

    COUNT_LETTERS = 0
    LETTER_COUNT = {}
    for word in WORDS:
        for c in word:
            if c in LETTER_COUNT:
                LETTER_COUNT[c] = LETTER_COUNT[c] + 1
            else:
                LETTER_COUNT[c] = 1
            COUNT_LETTERS = COUNT_LETTERS + 1

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
            PERCENT = ((100 *  WORD_COUNT[key]) / COUNT_LETTERS)
            LIMIT_PERCENT = round(PERCENT, 2)
            print(key + ' --> ' + str(LIMIT_PERCENT) + '%')
            LIMIT = LIMIT - 1
            if LIMIT < 0:
                break
    else:
        LIMIT = int(LIST_WORDS) - 1
        for key in WORD_COUNT:
            PERCENT = ((100 *  WORD_COUNT[key]) / COUNT_LETTERS)
            LIMIT_PERCENT = round(PERCENT, 2)
            print(key + ' --> ' + str(LIMIT_PERCENT) + '%')

    print('\n\n')
    



"""

print_list_words():     print the list of words used
argument:               list; WORD_USED is the list passed of all word used from the user
                        list; STRING_COMPARE is the list we use to compare the string with the data we have
return:

"""

def print_list_words(WORD_USED, STRING_COMPARE_USED):
    i = 0
    print("\nLista di parole usate:")
    for w in WORD_USED:
        if i < len(WORD_USED) - 1:
            print(w, end=', ')
        else:
            print(w)
        i = i + 1

    i = 0
    for s in STRING_COMPARE_USED:
        if i < len(STRING_COMPARE_USED) - 1:
            print(s, end=', ')
        else:
            print(s, '\n\n')
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
return:                 null

"""

def start():

    LIST_WORDS = input("Inserisci la lunghezza della parola da indovinare (tra 4 e 9 caratteri): \n")
    ALLOW = "456789"

    while len(str(LIST_WORDS)) != 1 or not str(LIST_WORDS).isdecimal() or not all(ch in ALLOW for ch in LIST_WORDS):
        LIST_WORDS = ""
        LIST_WORDS = input("Devi inserire la lunghezza della parola da indovinare (tra 4 e 9 caratteri): \n")

    LIST_WORDS_ALL = "./list/lista_" + str(LIST_WORDS) + "_wordle_ita.txt"
    INPUT = open(LIST_WORDS_ALL, "r")
    WORDS = set()

    for word in INPUT:
        WORDS.add(word.strip())

    INPUT.close()

    SELECTED = input("Inserisci:\n\t0 per testare\n\t1 per barare\n\t2 per giocare\n")
    SELECT_ALLOW = "012"

    while len(str(LIST_WORDS)) != 1 or not str(SELECTED).isdecimal() or not all(ch in SELECT_ALLOW for ch in SELECTED):
        SELECTED = ""
        SELECTED = input("Devi inserire:\n\t0 per testare\n\t1 per barare\n\t2 per giocare\n")

    if int(SELECTED) == 1:
        resolve(WORDS, LIST_WORDS)
    elif int(SELECTED) == 2:
        play(WORDS, LIST_WORDS)
    else:
        NEW_INPUT = "./list/lista_" + str(LIST_WORDS) + "_wordle_ita.txt"
        INPUT = open(NEW_INPUT, "r")

        FIRST_WORD = create_first_word(WORDS, LIST_WORDS, "")

        temp_words = WORDS.copy()

        for target_word in INPUT:
            target_word = target_word.replace('\n', '')
            TESTER = automatic_resolve(WORDS, LIST_WORDS, FIRST_WORD, target_word)

            WORDS = temp_words.copy()


            print(target_word + " " + str(TESTER))

"""
play:                       play the actual game wordle in italian
argument:                   map; words the map of all the possible Words
                            int; LIST_WORDS who represent the length of the word
return:                     null;
"""

def play(words, list_words):
    print("ciao")


"""
automatic_resolve:          try to automatate the process of resolving wordle game
argument:                   map; WORDS the map of all the possible Words
                            int; LIST_WORDS who represent the length of the word
                            str; FIRST_WORD is the first word used to start the game
                            str; target_word is the target word we wanna find
return:                     int; how many steps to take from the first word to the target word
"""

def automatic_resolve(words, LIST_WORDS, FIRST_WORD, target_word):

    STRING_INDEX = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    MATRIX = create_map(LIST_WORDS)
    CHAR_ONE = []


    WORD = FIRST_WORD
    STRING_COMPARE = string_compare(WORD, target_word)
    TOT = 1

    while len(words) > 1:

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

        for word in words.copy():
            for c in range(0, int(LIST_WORDS)):
                NUMBER = STRING_INDEX[word[c]]
                if MATRIX[NUMBER][c] == 0:
                    words.remove(word)
                    break

        """
        remove the words that doesn't contain the letter needed
        """

        for word in words.copy():
            for w in CHAR_ONE:
                if w not in word:
                    words.remove(word)
                    break


        if len(words) == 1:
            return TOT
        elif len(words) > 1:
            WORD = automatic_optimize(words, LIST_WORDS)
            STRING_COMPARE = string_compare(WORD, target_word)
            TOT = TOT + 1

    return -1

"""
automatic_optimize      optimize automatically the process of best word
argument:               set; WORDS the set of the possible words
                        string; LIST_WORDS is the length of word
return:                 string; return the string with the most valuable points

"""

def automatic_optimize(WORDS, LIST_WORDS):

    """
    Step1: create a map which count the frequency of the letters that appear in each word and sort it in descending order
    """

    COUNT_LETTERS = 0
    LETTER_COUNT = {}
    for word in WORDS:
        for c in word:
            if c in LETTER_COUNT:
                LETTER_COUNT[c] = LETTER_COUNT[c] + 1
            else:
                LETTER_COUNT[c] = 1
            COUNT_LETTERS = COUNT_LETTERS + 1

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

    return str(list(WORD_COUNT.keys())[0])



"""
string_compare:             take 2 strings and confront them generating the string we need, compoed by 0, 1 or 2
argument:                   str; STRING_1 the first string
                            str; STRING_2 the ipothetic "correct" string
return:                     str; the string formed by 0, 1 or 2
"""

def string_compare(STRING_1, STRING_2):
    STRING_TOT = ""

    for i in range(0, len(STRING_1)):
        FOUND = False
        for j in range(0, len(STRING_2)):
            if STRING_1[i] == STRING_2[i]:
                STRING_TOT = STRING_TOT + str(2)
                FOUND = True
                break
            else:
                if STRING_1[i] == STRING_2[j]:
                    STRING_TOT = STRING_TOT + str(1)
                    FOUND = True
                    break

        if not FOUND:
            STRING_TOT = STRING_TOT + str(0)

    return STRING_TOT


if __name__ == "__main__":
    main()
