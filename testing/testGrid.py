grid = []
row = []

for i in range(9):
  grid.append([])

for i in range(9):
  for i in range(9):
    grid[i].append(' ')

def gameBoard():
  print("-----------")
  for i in range(9):
    print("|",end = '')
    print(grid[0][i],end = '')
    print(grid[1][i],end = '')
    print(grid[2][i],end = '')
    print(grid[3][i],end = '')
    print(grid[4][i],end = '')
    print(grid[5][i],end = '')
    print(grid[6][i],end = '')
    print(grid[7][i],end = '')
    print(grid[8][i],end = '')
    print("|")
  print("-----------")

gameBoard()
grid[3][4] = "*"
gameBoard()