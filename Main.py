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

consoleWidth, consoleheight = shutil.get_terminal_size() #calculates terminal height and width 


def gameDisp(text):     #whatever text is given gets displayed in center of terminal
  global consoleWidth
  x = text.center(consoleWidth)
  print(x, sep=" ", end="\t")


# userName = input("what is your name")
# print(f"Hello there {userName}")
# tim.sleep(0.7)
# print("By the way my name is Luke Emia")
# tim.sleep(0.7)
# print("you may call me luke")

symbols = ["cherry", "diamond", "heart", "banana", "chappal", "coffee", "tree"]
empty = "X"
imageReel = []


def hype() -> None:   #some text to keep them in
  tim.sleep(1)
  print("Get ready with your gambling Addiction")


def denominator(factor, money): #gambling term just google
  credit = money / factor
  return credits


def slot() -> str:    #generates 1 symbol for the possible 3 slots 
  global empty
  global symbols
  slots = 0
  probability = random.randint(0, 10)

  if probability < 6:
    slots = random.choice(symbols)
  else:
    slots = empty
  return str(slots)


def cursorSpin()->None:    #A spinning cursor animation,it spits None when animation is over ,need to fix that

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


def startMachine() -> None:     #displays the symbol       
  gameDisp("--------------------------")
  
  gameDisp(displayReel)
  gameDisp("--------------------------")


startMachine()

def startGame():    #starts game on enter
  while True:
    key.wait('enter')    
    startMachine()
