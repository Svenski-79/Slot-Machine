import sys
import time as tim
import shutil
import keyboard as key

# Initialize
consoleWidth, consoleheight = shutil.get_terminal_size()
symbols = ["cherry", "diamond", "heart", "banana", "chappal", "coffee", "tree"]
Lsymbols = len(symbols)


def update(text):  # whatever text is given gets displayed in center of terminal
    global consoleWidth
    x = text.center(consoleWidth)
    print("\r", end="")
    print(x, end="")
    tim.sleep(.1)

def stringBuild():
    d

key.wait('enter')
for i in range(10):
    update(symbols[i%Lsymbols])
    
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

