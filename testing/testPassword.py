def na():
  email = input('Enter email address: ')
  pwd = input('Enter password: ')
  conf_pwd = input('Confirm password: ')
  if conf_pwd == pwd:
      with open('credentials.txt', 'w') as data:
           data.write(email + '\n')
           data.write(pwd)
      data.close()
      print('You have registered successfully!')
  else:
      print('Password is not same as above! \n')

with open('credentials.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    print(data[0])
    n = 0
  
    while data[n] != '.':
      n += 1
    print(n)

email = 'N/A'
pwd = 'N/A'

data[n - 1] = email
data[n] = pwd
with open('credentials.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)