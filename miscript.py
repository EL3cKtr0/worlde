INPUT_FILE = "./input/660000_parole_italiane.txt"
FIRST = "./list/lista_"
THIRD = "_wordle_ita.txt"

def create_files():
    for c in range(4, 10):
        NAME_OUTPUT = FIRST + str(c) + THIRD
        OUTPUT = open(NAME_OUTPUT, "w")
        OUTPUT.close()

def write_on_file(c, name):
    INPUT = open(INPUT_FILE, "r")
    OUT = open(name, "w")
    for word in INPUT:
        if len(word) == c + 1:
            OUT.write(word)
    INPUT.close()
    OUT.close()

print("Generating files..")
create_files()

print("Writing on files..")
for c in range(4, 10):
    NAME_OUTPUT = FIRST + str(c) + THIRD
    write_on_file(c, NAME_OUTPUT)


print("List of Words Generated")
