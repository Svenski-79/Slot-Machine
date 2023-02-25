import time as tim
import shutil
import random
import keyboard as key 

# Initialize
consoleWidth, consoleheight = shutil.get_terminal_size()
symbols = ["cherry", "diamond", "heart", "banana", "chappal", "coffee", "tree"]
Lsymbols = len(symbols)


def update(text):  # whatever text is given gets displayed in center of terminal
    global consoleWidth
    print("\r", end="")
    print(text, end="")
    tim.sleep(.1)

def stringBuild(str1="START", str2="START", str3="START"):
    STR = str1.center(10) + str2.center(10) + str3.center(10)
    return(STR.center(consoleWidth))

def gameOn() -> str:
    str = ["START", "START", "START"]
    for i in range(3):
        while True:
            choice = random.choice
            str1 = symbols(choice) if choice < Lsymbols else "Empty"
            update(stringBuild(str[0], str[2], str[3]))
    return str

def GameON():
    for r in int(input("Rounds : ")):
        gameOn()

GameON()
# sys.stdout.write('hello')
# sys.stdout.flush()
# for _ in range(5):
#     time.sleep(1)
#     sys.stdout.write('\033[D \033[D')
#     sys.stdout.flush()

# print("boss")
# time.sleep(1)
# sys.stdout.flush()


# for i in range(20):
#     print(symbols[i%Lsymbols], end="")
#     # sys.stdout.flush()
#     print("\r",end="")
#     time.sleep(.05)

# for x in range(10):
#     print("Grape \r",end="")

