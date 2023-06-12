import getpass

def signup():
    username = input('Enter username: ')
    pwd = getpass.getpass('Enter password: ')
    conf_pwd = getpass.getpass('Confirm password: ')
    
    if conf_pwd == pwd:
        with open('credentials.txt', 'a') as file:
            file.write(username + '\n')
            file.write(pwd + '\n')
        
        print('You have registered successfully!')
    else:
        print('Password is not the same as above!')

def login():
    username = input('Enter username: ')
    pwd = getpass.getpass('Enter password: ')
    
    with open('credentials.txt', 'r') as file:
        data = file.readlines()
        
        i = 0
        while i < len(data):
            if data[i].strip() == username and data[i+1].strip() == pwd:
                print('Login Successful!')
                return
            i += 2
        
        print('Login Unsuccessful!')

choice = int(input('1. Signup 2. Login -> '))
if choice == 1:
    signup()
elif choice == 2:
    login()
else:
    print('Not an option')
