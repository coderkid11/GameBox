import time
import os
import sys
from asciiArt.asciiLogo import asciiLogo
from asciiArt.asciiLogo import slowAsciiLogo
from games.rockPaperScissors import rockPaperScissors

def pickGame():
  print("Pick your game from the list below:")
  
  print("1. Rock Paper Scissors")
  print("2. Tic Tac Toe")
  print("3. N/A")
  print("4. N/A")
  print("5. N/A")
  
  print(" ")
  gameChoice = input("Enter your game number: ")
  os.system('clear')
  asciiLogo()
  
  if gameChoice == "1":
    print("You chose " + gameChoice)
    print("Good Choice!")
    print("Transporting in")
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(0.5)
    print("Here we goooooooooo!")
    time.sleep(0.5)
    rockPaperScissors()
    os.system('clear')
    asciiLogo()
  elif gameChoice == "2":
    print("Good Choice!")
    print("Transporting in")
    print(3)
    time.sleep(0.5)
    print(2)
    time.sleep(0.5)
    print(1)
    time.sleep(0.5)
    print("Here we goooooooooo!")
    time.sleep(1)
    print("Unfortunately GameBox doesn't seem to have access to this game right now.")
    print("")
  else:
    pass

slowAsciiLogo()
print("Welcome To GameBox!")
print(" ")
print("This is a developing service with games being coded every week!")
enterToContinue = input("Press ENTER to continue ")
os.system('clear')

while True:
  os.system('clear')
  asciiLogo()
  pickGame()
  if input('Do you want to play another game? (y/n)? ') not in ('Y','y'):
    os.system('clear')
    asciiLogo()
    words = ("Thanks for playing!")
    for char in words:
      time.sleep(0.1)
      sys.stdout.write(char)
      sys.stdout.flush()
    print("")
    break