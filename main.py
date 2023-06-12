import time
import os
import sys
from asciiArt.asciiLogo import asciiLogo
from asciiArt.asciiLogo import slowAsciiLogo
from games.rockPaperScissors import rockPaperScissors
from games.chaseGame import chaseGame

def signup():
    email = input('Enter email address: ')
    pwd = input('Enter password: ')
    conf_pwd = input('Confirm password: ')
    if conf_pwd == pwd:
        with open('credentials.txt', 'w') as f:
             f.write(email + '\n')
             f.write(pwd)
        f.close()
        print('You have registered successfully!')
    else:
        print('Password is not same as above! \n')
    os.system('clear')  

def login():
    global loginSuccesful
    email = input('Enter email: ')
    pwd = input('Enter password: ')
    with open('credentials.txt', 'r') as f:
        stored_email, stored_pwd = f.read().split('\n')
    f.close()
    if email == stored_email and pwd == stored_pwd:
         print('Logged in Successfully!')
         loginSuccesful = True
    else:
         print('Login failed! \n')
    wait = input('Press ENTER to continue')
    os.system('clear')

def loginMenu():
  global loginSuccesful
  while 1:
    asciiLogo()
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    print('')
    ch = int(input("Enter your choice: "))
    os.system('clear')
    asciiLogo()
    
    if ch == 1:
        signup()
    elif ch == 2:
        login()
        if loginSuccesful == True:
          break
    elif ch == 3:
        os.system('clear')
        asciiLogo()
        words = ("Thanks for playing!")
        for char in words:
          time.sleep(0.1)
          sys.stdout.write(char)
          sys.stdout.flush()
        print("")
        exit()
    else:
        print("Wrong Choice!")

def pickGame():
  print("Pick your game from the list below:")
  
  print("1. Rock Paper Scissors")
  print("2. Chase Game")
  print("3. N/A")
  print("4. N/A")
  print("5. N/A")
  
  print(" ")
  gameChoice = input("Enter your game number: ")
  os.system('clear')
  asciiLogo()
  
  if gameChoice == "1":
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
    time.sleep(0.5)
    chaseGame()
  else:
    pass

slowAsciiLogo()
print("Welcome To GameBox!")
print(" ")
print("This is a developing service with games being coded every week!")
enterToContinue = input("Press ENTER to continue ")
os.system('clear')
loginMenu()

while True:
  os.system('clear')
  asciiLogo()
  pickGame()
  os.system('clear')
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