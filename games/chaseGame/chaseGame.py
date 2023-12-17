from readchar import readkey
from asciiArt.asciiLogo import asciiLogo
from asciiArt.asciiLogo import slowAsciiLogo
from asciiArt.treasureChest import treasureChest
import os
import random
import time


def customization():
    global gridWidth
    global gridLength
    global botMovementRandomness
    global playerCharacter
    global botCharacter

    # print(f"Hello there, {username}, welcome to the Chase Game!")
    # print()

    print('1. Easy 2. Medium 3. Difficult 4. Impossible')
    difficulty = int(input('Pick a difficulty number -> '))

    if difficulty == 1:
        gridWidth = 80
        gridLength = 25
        botMovementRandomness = 4
    elif difficulty == 2:
        gridWidth = 40
        gridLength = 10
        botMovementRandomness = 3
    elif difficulty == 3:
        gridWidth = 20
        gridLength = 5
        botMovementRandomness = 1
    elif difficulty == 4:
        gridWidth = 10
        gridLength = 3
        botMovementRandomness = 1

    print('1.☆ 2.× 3.♢ 4.♔ 5.♕')
    playerCharacter = int(input('Pick your character number -> '))

    if playerCharacter == 1:
        playerCharacter = '☆'
    elif playerCharacter == 2:
        playerCharacter = '×'
    elif playerCharacter == 3:
        playerCharacter = '♢'
    elif playerCharacter == 4:
        playerCharacter = '♔'
    elif playerCharacter == 5:
        playerCharacter = '♕'

    print('1.★ 2.╳ 3.♤ 4.♚ 5.♛')
    botCharacter = int(input('Pick your bot character number -> '))

    if botCharacter == 1:
        botCharacter = '★'
    elif botCharacter == 2:
        botCharacter = '╳'
    elif botCharacter == 3:
        botCharacter = '♤'
    elif botCharacter == 4:
        botCharacter = '♚'
    elif botCharacter == 5:
        botCharacter = '♛'


def everythingRestart():
    global coordsX
    global coordsY
    coordsX = (0)
    coordsY = (0)

    global botCoordsX
    global botCoordsY
    botCoordsX = random.randint(0, (gridWidth))
    botCoordsY = random.randint(0, (gridLength))

    global gameLose
    gameLose = 'n'

    global numOfMoves
    numOfMoves = 0

    global powerUpUsed
    powerUpUsed = True

    global powerUpCoordsX
    powerUpCoordsX = gridWidth + 10

    global powerUpCoordsY
    powerUpCoordsY = gridLength + 10

    global speedMultiplier
    speedMultiplier = 1

    global powerUpInUse
    powerUpInUse = False

    global finishCoordsX, finishCoordsY
    finishCoordsX = random.randint(5, gridWidth - 1)
    finishCoordsY = random.randint(0, gridLength - 1)


def createGameBoard():
    global grid
    grid = []
    for i in range(gridWidth):
        grid.append([])

    for i in range(gridWidth):
        for i in range(gridWidth):
            grid[i].append(' ')


def keyMove():
    global coordsX, coordsY, numOfMoves, powerUpInUse, speedMultiplier
    while True:
        key = readkey()
        print(key)
        if key == '\x1b[A':
            key = "up"

            if coordsY == 0:
                pass
            elif powerUpInUse == True and coordsY == gridLength + speedMultiplier:
                pass
            else:
                coordsY = coordsY - (1 * speedMultiplier)

        elif key == '\x1b[B':
            key = "down"

            if coordsY == (gridLength - 1):
                pass
            elif powerUpInUse == True and coordsY == gridLength - speedMultiplier:
                pass
            else:
                coordsY = coordsY + (1 * speedMultiplier)

        elif key == '\x1b[C':
            key = "right"

            if coordsX == (gridWidth - 1):
                pass
            elif powerUpInUse == True and coordsX == gridWidth + speedMultiplier:
                pass
            else:
                coordsX = coordsX + (1 * speedMultiplier)

        elif key == '\x1b[D':
            key = "left"

            if coordsX == 0:
                pass
            elif powerUpInUse == True and coordsX == gridWidth + speedMultiplier:
                pass
            else:
                coordsX = coordsX - (1 * speedMultiplier)

        elif key == 'e':
            os.system('clear')
            exit()

        numOfMoves = numOfMoves + 1
        break


def gameBoardLogic(username):
    global coordsX, coordsY, gameLose, botCoordsX, botCoordsY, powerUpCoordsX, powerUpCoordsY, powerUpUsed, numOfMoves, speedMultiplier, powerUpInUse, finishCoordsX, finishCoordsY, botMovementRandomness, playerCharacter, powerUpNumOfMoves
    createGameBoard()

    if powerUpUsed == False:
        grid[powerUpCoordsX][powerUpCoordsY] = '!'
    else:
        pass

    grid[coordsX][coordsY] = playerCharacter
    grid[finishCoordsX][finishCoordsY] = '□'
    grid[botCoordsX][botCoordsY] = botCharacter

    if coordsX == botCoordsX and coordsY == botCoordsY:
        os.system('clear')
        print("You got caught!")
        gameLose = 'y'
    elif coordsX == finishCoordsX and coordsY == finishCoordsY:
        win(username)
        gameLose = 'y'
    elif coordsX == powerUpCoordsX and coordsY == powerUpCoordsY:
        print("You got a power up!")
        speedMultiplier = random.randint(2, 5)
        powerUpNumOfMoves = random.randint(1, 5)
        print(str(speedMultiplier) + "x Speed!")
        print("For " + str(powerUpNumOfMoves) + " moves!")
        powerUpUsed = True
        wait = input("Press ENTER to continue")
        powerUpCoordsX = gridWidth + 10
        powerUpCoordsY = gridLength + 10
        numOfMoves = 0
        powerUpInUse = True

    if numOfMoves >= 10 and random.randint(1, 3) == 3 and powerUpUsed == True:
        powerUpCoordsX = random.randint(coordsX, gridWidth)
        powerUpCoordsY = random.randint(coordsY, gridLength)
        powerUpUsed = False

    if powerUpInUse == True and numOfMoves == powerUpNumOfMoves:
        powerUpInUse = False
        speedMultiplier = 1
        numOfMoves = 0


def printGameBoard():
    print("Use the arrow keys to move to the bottom corner or press E to exit:")
    for i in range(gridWidth):
        print("-", end='')
    print("--")
    for i in range(gridLength):
        print("|", end='')

        for a in range(gridWidth):
            print(grid[a][i], end='')
        print("|")
    for i in range(gridWidth):
        print("-", end='')
    print("--")


def botMovement():
    global botCoordsY, botCoordsX, coordsY, coordsX

    yLockedOn = 'n'

    if random.randint(1, 3) == 3:
        if coordsY > botCoordsY:
            botCoordsY = botCoordsY + 1
        elif coordsY < botCoordsY:
            botCoordsY = botCoordsY - 1
        else:
            yLockedOn = 'y'

    if random.randint(1, 2) == 2:
        yLockedOn = 'y'

    if yLockedOn == 'y':
        if coordsX > botCoordsX:
            botCoordsX = botCoordsX + 2
        elif coordsX < botCoordsX:
            botCoordsX = botCoordsX - 1
    else:
        pass


def win(username):
    os.system('clear')
    print("You got the treasure without being caught!")
    print()
    treasureChest()
    print()

    with open('games/chaseGame/chaseScores.txt', 'r') as file:
        data = file.readlines()

    for i in range(len(data)):
        if username in data[i].strip():
            data[i] = username + " " + str(numOfMoves) + "\n"
            break

    with open('games/chaseGame/chaseScores.txt', 'a') as file:
        file.writelines(data)

# Running Code


def chaseGame(username):
    global gameLose
    os.system('clear')
    global difficulty
    global botMovementRandomness

    asciiLogo()
    customization()
    everythingRestart()

    while True:
        os.system('clear')
        gameBoardLogic(username)
        printGameBoard()
        keyMove()
        os.system('clear')
        botMovement()
        gameBoardLogic(username)
        if gameLose == 'n':
            printGameBoard()
        elif gameLose == 'y':
            if input('Play again (y/n)? ') not in ('Y', 'y'):
                print('Thanks for playing!')
                break
            else:
                customizationYorN = input(
                    'Do you want to customize your settings (y/n)? ')
                if customizationYorN == ('Y', 'y'):
                    customization()
                    gameLose = 'n'
                    everythingRestart()
                else:
                    gameLose = 'n'
                    everythingRestart()
