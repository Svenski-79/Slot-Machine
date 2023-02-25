# need a credit System for user money
# 3 different betting denominator
# 7 different symbols
# 3 reels
# reward table
import sys
import time as tim
import random
import keyboard as key
import shutil

# calculates terminal height and width
consoleWidth, consoleheight = shutil.get_terminal_size()
symbols = ["cherry", "diamond", "heart", "banana", "chappal", "coffee", "tree"]
empty = "X"
imageReel = []

def gameDisp(text):  # whatever text is given gets displayed in center of terminal
    global consoleWidth
    x = text.center(consoleWidth)
    print(x, sep="", end="")


def update(text):  # whatever text is given gets displayed in center of terminal
    global consoleWidth
    print("\r", end="")
    tim.sleep(.05)
    x = text.center(consoleWidth)
    print(x, end="")

def hype() -> None:  # some text to keep them in
    tim.sleep(1)
    print("Get ready with your gambling Addiction")

def denominator(factor, money):  # gambling term just google
    credit = money/factor
    return credits

def slot() -> str:  # generates 1 symbol for the possible 3 slots
    global empty
    global symbols
    probability = random.randint(0, 10)
    return str(symbols[probability] if probability < 6 else empty)

def cursorSpin() -> None:  # A spinning cursor animation,it spits None when animation is over ,need to fix that

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor

    spinner = spinning_cursor()
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        tim.sleep(0.1)
        sys.stdout.write('\b')
        if


def startMachine() -> None:  # displays the symbol
    gameDisp("--------------------------")

    gameDisp(displayReel)
    gameDisp("--------------------------")

def startGame():  # starts game on enter
    while True:
        key.wait('enter')
        startMachine()
        

startMachine()

gameDisp("START")
for i in range(10):
    print("\r")
    gameDisp0(symbols[i])
    tim.sleep(.1)
sys.stdout.flush()

