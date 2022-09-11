import os

os.system('cls')

# functions here
# ==============================

# Check menu input value
def checkinput():
    while True:
        try:
            val = int(input())
        except ValueError:
            print('Pls Enter a number!\n')
            continue
        else:
            if val > 2 or val < 1:
                print('Enter a Number 1 or 2 !\n')
            else:
                return val

# Check username and password
def checkLoginUser(username, password):
    file = open('users.txt', 'r')
    userExist = False
    
    for line in file:
        
        userData = line.split(':')
        un = userData[0]
        up = userData[1].replace('\n', '')
        
        # check file data
        if un == username and up == password:
            userExist = True
    
    if userExist == False:
        print('Invalid username or password!\n')       
    
    file.close()
    return userExist

# Login Menu, check username and password
def loginPanel():
    while True:
        print('Login Panel')
        un = input('Username: ')
        up = input('Password: ')

        # check username and password
        if checkLoginUser(un, up):
            print('Welcome', un, '!')
            break

# Check this username is exist
def checkRegUsername(username):
    file = open('users.txt', 'r')
    for line in file:
        data = line.split(':')
        if data[0] == username:
            print('Username is already taken!\n')
            file.close()
            return True
        
    file.close()
    return False

# Register menu, check this username is exist
def registerPanel():
    while True:
        
        print('Register Panel\n')
        regUser = input('New Username: ')
        regPass = input('New Password: ')
        
        # Check this username is exist
        if not checkRegUsername(regUser):
            
            file = open('users.txt', 'a')
            data = regUser + ':' + regPass
            file.write(data + '\n')
            file.close()
            
            print('You can Loging in!\n')
            
            break
        
    
# Program start
# ==============================
while True:
    print('Login System\n')
    print('Enter a number 1 or 2!\n')
    print('1. Login')
    print('2. Register\n')

    # Check input value
    userInput = checkinput()

    # Login user
    if userInput == 1:
        loginPanel()
        break

    # Register user
    if userInput == 2:
        registerPanel()
