import getpass
import os
import sys
import time

from asciiArt.asciiLogo import asciiLogo, slowAsciiLogo
from games.chaseGame.chaseGame import chaseGame
from games.rockPaperScissors.rockPaperScissors import rockPaperScissors


def signup():
    username = input("Enter username: ")
    pwd = getpass.getpass("Enter password: ")
    conf_pwd = getpass.getpass("Confirm password: ")

    if conf_pwd == pwd:
        with open("credentials.txt", "a") as file:
            file.write(username + "\n")
            file.write(pwd + "\n")

        with open("games/chaseGame/chaseScores.txt", "a") as file:
            file.write(username + ",0" + "\n")

        with open("games/rockPaperScissors/rockPaperScissorsScores.txt", "a") as file:
            file.write(username + ",0" + "\n")

        print("You have registered successfully!")
    else:
        print("Password is not the same as above!")


def login():
    global loginSuccesful
    global username
    username = input("Enter username: ")
    pwd = getpass.getpass("Enter password: ")

    with open("credentials.txt", "r") as file:
        data = file.readlines()

        i = 0
        while i < len(data):
            if data[i].strip() == username and data[i + 1].strip() == pwd:
                print("Login Successful!")
                loginSuccesful = True
                return
            i += 2

        print("Login Unsuccessful!")


def loginMenu():
    global loginSuccesful
    while 1:
        asciiLogo()
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        print("")
        ch = int(input("Enter your choice: "))
        os.system("clear")
        asciiLogo()

        if ch == 1:
            signup()
            os.system("clear")
        elif ch == 2:
            login()
            if loginSuccesful == True:
                os.system("clear")
                break
        elif ch == 3:
            os.system("clear")
            asciiLogo()
            words = "Thanks for playing!"
            for char in words:
                time.sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()
            print("")
            exit()
        else:
            print("Wrong Choice!")


def pickGame():
    print("Hello " + username + "!")
    print()
    print("Pick your game from the list below:")

    print("1. Rock Paper Scissors")
    print("2. Chase Game")
    print("3. N/A")
    print("4. N/A")
    print("5. N/A")

    print(" ")
    gameChoice = input("Enter your game number: ")
    os.system("clear")
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
        os.system("clear")
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
        chaseGame(username)
    else:
        pass


try:
    os.system("clear")
    slowAsciiLogo()
    print("Welcome To GameBox!")
    print(" ")
    print("This is a developing service with games being coded every week!")
    enterToContinue = input("Press ENTER to continue ")
    os.system("clear")
    loginMenu()

    while True:
        os.system("clear")
        asciiLogo()
        pickGame()
        os.system("clear")
        if input("Do you want to play another game? (y/n)? ") not in ("Y", "y"):
            os.system("clear")
            asciiLogo()
            words = "Thanks for playing!"
            for char in words:
                time.sleep(0.1)
                sys.stdout.write(char)
                sys.stdout.flush()
            print("")
            break
except:
    os.system("clear")
    print("There was an error. Please try again.")
    print("Contact the developer if this keeps happening.")
