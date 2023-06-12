import os
import time
from readchar import readkey

def resetVariables():
  global gridWidth, gridHeight, grid, playerCoordsX, playerCoordsY, numOfMoves, snakeLength, direction
  gridWidth = 70
  gridHeight = 20

  playerCoordsX = 10
  playerCoordsY = 10
  
  numOfMoves = 0

  snakeLength = 3

  direction = 'right'

def createGameBoard():
  global gridWidth, gridHeight, grid
  grid = []
  for i in range(gridWidth):
    grid.append([])
  
  for i in range(gridWidth):
    for i in range(gridWidth):
      grid[i].append(' ')

def keyMove():
  global gridLength, gridWidth, playerCoordsX, playerCoordsY, numOfMoves, direction
  while True:
    key = readkey()
    print(key)
    if key == '\x1b[A':
      direction = 'up'

    elif key == '\x1b[B':
      direction = 'down'
      
    elif key == '\x1b[C':
      direction = 'left'
    
    elif key == '\x1b[D':
      direction = 'right'
      
    elif key == 'e':
      os.system('clear')
      exit()
    
    numOfMoves = numOfMoves + 1
    break


def printGameBoard():
  global gridWidth, gridHeight, grid
  print("Use the arrow keys to move or press E to exit:")
  for i in range(gridWidth):
      print("-", end ='')
  print("--")
  for i in range(gridHeight):
    print("|",end = '')

    for a in range(gridWidth):
      print(grid[a][i],end = '')
    print("|")
  for i in range(gridWidth):
      print("-", end ='')
  print("--")

def playerMovement():
  global grid, playerCoordsX, playerCoordsY, gridLength, gridWidth, gridHeight, snakeLength, snakeBodyX, snakeBodyY, direction

  snakeBodyX = playerCoordsX
  snakeBodyY = playerCoordsY
  grid[playerCoordsX][playerCoordsY] = 'o'
  
  for i in range(1, snakeLength):
    if direction == 'up':
      snakeBodyY = playerCoordsY + i
    elif direction == 'down':
      snakeBodyY = playerCoordsY - i
    elif direction == 'right':
      snakeBodyX = playerCoordsX + i
    elif direction == 'left':
      snakeBodyX = playerCoordsX - i
    
    grid[snakeBodyX][snakeBodyY] = '='

def animation():
  global grid, gridWidth, gridHeight, snakeBodyX, snakeBodyY, direction, snakeLength, playerCoordsX, playerCoordsY, time

  timeGone = 0
  while timeGone !=10:
    playerCoordsX = playerCoordsX + 1
    time.sleep(1)
    os.system('clear')
    playerMovement()
    printGameBoard()
    keyMove()
    
  
os.system('clear')
resetVariables()
createGameBoard()
printGameBoard()
keyMove()
playerMovement()
os.system('clear')
printGameBoard()
animation()