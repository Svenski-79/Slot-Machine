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

consoleWidth, consoleheight = shutil.get_terminal_size(
)  #calculates terminal height and width


def typed(text) -> str:
  global consoleWidth
  para = text.center(consoleWidth)
  for i in para:
    print(i, end='', flush=True)
    tim.sleep(0.05)
  # print('\n')


def gameDisp(text):  # centralized text
  global consoleWidth
  x = text.center(consoleWidth)
  print(x, sep=" ")


def gameInput(text):
  global consoleWidth
  leftMargin = (consoleWidth - len(text)) // 2 - 6
  x = " " * leftMargin + text
  Input = input(x)
  return Input


symbols = {
  "cherry": 4,
  "diamond": 5,
  "heart": 3,
  "banana": 2,
  "chappal": 1,
  "coffee": 2,
  "tree": 1,
  "X": 0
}
imageReel = []


def hype() -> None:  #some text to keep them in
  tim.sleep(1)
  print("Get ready with your gambling Addiction")


def greedCheck(fee):
  if int(fee) > 1000:
    print("\n")
    typed("I might have to see your bank balance are you for real?!")
    typed("Do you really have that much money?(y/n)")
    result = gameInput("> ")

    if result == "y" or result == "yes" or "yes" in result: 
      return True
    else:
      typed("Ok bruh, enter a 'reasonable' amount")


def denominator(factor, money):  #gambling term just google
  credit = money / factor
  return credits


def slot() -> str:  #generates 1 symbol for the possible 3 slots
  global symbols
  slots = random.choice(symbols, weights=(42, 10, 42, 30, 35, 28, 33, 40))
  return slots


def cursorSpin(time) -> None:  #spin cursor

  def spinning_cursor():
    while True:
      for cursor in '|/-\\':
        yield cursor

  spinner = spinning_cursor()
  for i in range(time):
    for _ in range(4):
      sys.stdout.write(next(spinner))
      sys.stdout.flush()
      tim.sleep(0.1)
      sys.stdout.write('\b')


def startMachine() -> None:  #displays the symbol
  gameDisp("--------------------------")

  slot()
  gameDisp("--------------------------")
  return


def startGame():  #starts game on enter
  while True:
    typed("Hey what do you go by, I mean your name...?")
    name = gameInput("> ")
    typed(f"Hi {name}")

    while True:
      typed("How much money would you like to deposit : ")
      deposit = gameInput("> $")
      result = greedCheck(deposit)
      if result == True:
        print("")
        break
      
    # key.wait('enter')


startGame()
