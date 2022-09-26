
INPUT_FILE = "./input/660000_parole_italiane.txt"
FIRST = "./list/lista_"
THIRD = "_wordle_ita.txt"

def main():
    print("Generating files..")
    create_files()

    print("Writing on files..")
    writes()


    start()

"""

create_files():         create the files .txt of each lenght of words from 4 to 9
return:                 null;

"""

def create_files():
    for c in range(4, 10):
        NAME_OUTPUT = FIRST + str(c) + THIRD
        OUTPUT = open(NAME_OUTPUT, "w+")
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

    print("\n")
    return MY_WORD



"""

create_map():           create the map of all 1 for the confronting of the words
return:                 list of dict of dict; the structure for keep in memory the state of the words

"""

def create_map():
    HASHMAP = {}

    for i in range(0, 26):
        HASHMAP[i] = {}
        for j in range(0, 5):
            HASHMAP[i][j] = 1

    return HASHMAP


"""

create_string_3value(): create a string of 0, 1 or 2 to represent the letter which could, has or can't be in the word
return:                 string; the value of the string wiht 0, 1 or 2

"""

def create_string_3value():
    MY_WORD = input("Scrivi una stringa lunga 5 cosi formata:\n\t0 se la lettera nella corrispettiva posizione NON esiste\n\t1 se la lettera nella corrispettiva posizione ESISTE ma NON e' in quella posizione\n\t2 se la lettera nella corrispettiva posizione ESISTE ed e' in posizione CORRETTA\n")
    ALLOWED = "012"

    while len(str(MY_WORD)) != 5 or not str(MY_WORD).isdecimal() or not all(ch in ALLOWED for ch in MY_WORD):
        MY_WORD = str("")
        MY_WORD = input("ERRORE!\nScrivi una stringa lunga 5 cosi formata:\n\t0 se la lettera nella corrispettiva posizione NON esiste\n\t1 se la lettera nella corrispettiva posizione ESISTE ma NON e' in quella posizione\n\t2 se la lettera nella corrispettiva posizione ESISTE ed e' in posizione CORRETTA\n")
    
    print("\n")
    return MY_WORD



"""

resolve():              try to resolve the words cycling until the input contains only 1 word
argument:               set; the set of all the possible Words
return:                 

"""

def resolve(WORDS):

    INDEX_STRING = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}

    STRING_INDEX = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    MATRIX = create_map()
    CHAR_ONE = []


    while len(WORDS) > 1:
        WORD = create_first_word(WORDS)
        STRING_COMPARE = create_string_3value()
        
        for i in range(0, 5):
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
                for i in range(0, 5):
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
            for c in range(0, 5):
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

        print_set(WORDS)

    if len(WORDS) == 1:
        print("Congratulazioni! la parola e': " + WORDS.pop())
    else:
        print("Qualcosa e' andato storto, non e' stata trovata alcuna parola :(")



"""

print_set():            print the set in the argument
argument:               set; the set we wanna print
return:                 null


"""

def print_set(SET):
    i = 0
    for w in SET:
        if i < len(SET) - 1:
            print(w, end=', ')
        else:
            print(w + "\n")
        i = i + 1


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



if __name__ == "__main__":
    main()
