from readchar import readkey
import os
import random
import time

global gridWidth
gridWidth = 60

global gridLength
gridLength = 20

global coordsX
global coordsY
coordsX = (0)
coordsY = (0)

global botCoordsX
global botCoordsY
botCoordsX = random.randint(10,(gridWidth))
botCoordsY = random.randint(0,(gridLength))

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


def createGameBoard():
  global grid
  grid = []
  for i in range(gridWidth):
    grid.append([])
  
  for i in range(gridWidth):
    for i in range(gridWidth):
      grid[i].append(' ')

def keyMove():
  global coordsX, coordsY, numOfMoves
  while True:
    key = readkey()
    print(key)
    if key == '\x1b[A':
      key = "up"

      if coordsY == 0:
        pass
      else:
        coordsY = coordsY - (1 * speedMultiplier)
    
    elif key == '\x1b[B':
      key = "down"

      if coordsY == (gridLength - 1):
        pass
      else:
        coordsY = coordsY + (1 * speedMultiplier)
    
    elif key == '\x1b[C':
      key = "right"
    
      if coordsX == (gridWidth - 1):
        pass
      else:
        coordsX = coordsX + (1 * speedMultiplier)
    
    elif key == '\x1b[D':
      key = "left"
      
      if coordsX == 0:
        pass
      else:
        coordsX = coordsX - (1 * speedMultiplier)
    
    elif key == 'e':
      os.system('clear')
      exit()
    
    numOfMoves = numOfMoves + 1
    break

def gameBoardLogic():
  global coordsX, coordsY, gameLose, botCoordsX, botCoordsY, powerUpCoordsX, powerUpCoordsY, powerUpUsed, numOfMoves, speedMultiplier
  createGameBoard()

  if powerUpUsed == False:
    grid[powerUpCoordsX][powerUpCoordsY] = '!'
  else:
    pass
  
  grid[coordsX][coordsY] = '*'
  grid[botCoordsX][botCoordsY] = 'X'
  grid[gridWidth - 1][gridLength - 1] = '□'
    
  if coordsX == botCoordsX and coordsY == botCoordsY:
    os.system('clear')
    print("You got caught!")
    gameLose = 'y'
  elif coordsX == gridWidth - 1 and coordsY == gridLength - 1:
    os.system('clear')
    time.sleep(0.5)
    print("You got to the other side!")
    gameLose = 'y' 
  elif coordsX == powerUpCoordsX and coordsY == powerUpCoordsY:
    print("You got a power up!")
    speedMultiplier = random.randint(1,5)
    print(str(speedMultiplier) + "x Speed!")
    powerUpUsed = True
    wait = input("Press ENTER to continue")
    powerUpCoordsX = gridWidth + 10
    powerUpCoordsY = gridLength + 10
    numOfMoves = 0
  
  if numOfMoves >= 10 and random.randint(1,4) == 4 and powerUpUsed == True:
    powerUpCoordsX = random.randint(coordsX, gridWidth)
    powerUpCoordsY = random.randint(coordsY, gridLength)
    powerUpUsed = False
    
def printGameBoard():
  print("Use the arrow keys to move to the bottom corner or press E to exit:")
  for i in range(gridWidth):
      print("-", end ='')
  print("--")
  for i in range(gridLength):
    print("|",end = '')

    for a in range(gridWidth):
      print(grid[a][i],end = '')
    print("|")
  for i in range(gridWidth):
      print("-", end ='')
  print("-")

def botMovement():
  global botCoordsY, botCoordsX, coordsY, coordsX
  
  yLockedOn = 'n'

  if random.randint(1,2) == 2:
    if coordsY > botCoordsY:
      botCoordsY = botCoordsY + 1
    elif coordsY < botCoordsY:
      botCoordsY = botCoordsY - 1
    else:
      yLockedOn = 'y'

  if random.randint(1,2) == 2:
    yLockedOn = 'y'
    
  if yLockedOn == 'y':
    if coordsX > botCoordsX:
      botCoordsX = botCoordsX + 2
    elif coordsX < botCoordsX:
      botCoordsX = botCoordsX - 1
  else:
    pass

# Running Code

while True:
  os.system('clear')
  gameBoardLogic()
  printGameBoard()
  keyMove()
  os.system('clear')
  botMovement()
  gameBoardLogic()
  if gameLose == 'n':
    printGameBoard()
  else:
    break