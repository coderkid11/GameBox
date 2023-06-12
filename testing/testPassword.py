def signup():
  email = input('Enter email address: ')
  pwd = input('Enter password: ')
  conf_pwd = input('Confirm password: ')
  if conf_pwd == pwd:
      with open('credentials.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        n = 0
  
        while data[n] != '.':
          n += 1
  
        data[0] = str(int(data[0]) + 2) + '\n'
        data[n-1] = email + '\n'
        data[n] = pwd + '\n\n' + '.'
        with open('credentials.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
            file.close()
      print('You have registered successfully!')
  else:
      print('Password is not same as above! \n')

def login():
  email = input('Enter email: ')
  pwd = input('Enter password: ')
  with open('credentials.txt', 'r') as file:
    data = file.readlines()
    print(data[1])
    linesToCheck = int(data[0])
    i = 1

    while i < int(data[0]):
      if data[i] == email:
        print('Login Successful!')
      else:
        print('Unsuccessful')
      i += 1
  file.close()
  
choice = int(input('1. Signup 2. Login -> '))
if choice == 1:
  signup()
elif choice == 2:
  login()
else:
  print('Not an option')