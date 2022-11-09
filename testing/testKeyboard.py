from readchar import readkey

while True:
  a = readkey()
  print(a)
  if a == '\x1b[A':
    print("You pressed up.")
  elif a == '\x1b[B':
    print("You pressed down.")
  elif a == '\x1b[C':
    print("You pressed right.")
  elif a == '\x1b[D':
    print("You pressed left.")
  elif a == 'a':
    print("Exit")
  break