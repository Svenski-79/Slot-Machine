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
import threading 

consoleWidth, consoleheight = shutil.get_terminal_size() #calculates terminal height and width 


def gameDisp(text):     #whatever text is given gets displayed in center of terminal
  global consoleWidth
  x = text.center(consoleWidth)
  print(x, sep=" ", end="\t")

symbols = {"cherry":4,
           "diamond":5,
           "heart":3,
           "banana":2,
           "chappal":1,
           "coffee":2,
           "tree":1,
           "X":0}
imageReel = []


def hype() -> None:   #some text to keep them in
  tim.sleep(1)
  print("Get ready with your gambling Addiction")


def denominator(factor, money): #gambling term just google
  credit = money / factor
  return credits


def slot() -> str:    #generates 1 symbol for the possible 3 slots 
  global symbols
  slots = random.choice(symbols,weights=(42,10,42,30,35,28,33,40))
  return slots


def cursorSpin(time)->None:    #A spinning cursor animation,it spits None when animation is over ,need to fix that

  def spinning_cursor():
    while True:
      for cursor in '|/-\\':
        yield cursor

  spinner = spinning_cursor()
  for i in range (time):
    for _ in range(4):
      sys.stdout.write(next(spinner))
      sys.stdout.flush()
      tim.sleep(0.1)
      sys.stdout.write('\b')
  


def startMachine() -> None:    #displays the symbol       
  gameDisp("--------------------------")
  reel1 = slot()
  reel2=slot()
  reel3 = slot()
  

  slot()
  gameDisp("--------------------------")

def startGame():    #starts game on enter
  while True:
    key.wait('enter')    
    startMachine()
