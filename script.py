#NOTE
#Different key for Username and password??
#Add option for path to find themselves

import os
from cryptography.fernet import Fernet
import time

#---Defines---


def choice():
    choice = input('What do you want to do \n * Decode Username and Password (d) \n * Encode username and password (e) \n')
    if choice == 'e':
        encodeDB()
    else:
        decodeDB() 

    
def findDB():
    txtFileNames = []

    for x in range(0,len(files)):
        if files[x] == 'db.txt':
            txtFileNames.append(files[x])
        else:
            pass

    if len(txtFileNames) > 1:
        print('Found ', len(txtFileNames), ' db files.')
        print('There are ', len(txtFileNames), ' db files ', txtFileNames,' which one would you like to use (Please choose a number between 1 and', len(txtFileNames))
        choiceFile = int(input())
        userTxtFile = txtFileNames[choiceFile-1]
        
    elif len(txtFileNames) == 0:
        print('No db Files found')
        dbMake = input('Can you locate the files? (y/n)')
        if dbMake == "y":
            #Add option to find it theirselves
            pass
        else:
            print('File will be created in this directory in when writing to. ')
            #should create file when tries to access
            userTxtFile = ''
    else:
        print('Found database file')
        userTxtFile = txtFileNames[0]

    return userTxtFile


def encodeDB():
    with open(userFileKey, 'rb') as f:
        userKey = f.read() 
        
    with open(passFileKey, 'rb') as f:
        passKey = f.read() 

    if findDB() == '':
        dbFileLoc = './db.txt'
    else:
        dbFileLoc = './'+findDB()

    dbfile = open(dbFileLoc, 'a') #undefined but I know this fix when get back by adding if blank add a new file location in directory
    appName = input('Name of App: ')
    username = input('Username of App: ').encode()
    password = input('Password of App: ').encode()

    u = Fernet(userKey)
    p = Fernet(passKey)

    encUsername = u.encrypt(username)
    encPassword = p.encrypt(password)


    print(encUsername)
    print(str(encUsername))
    print(encPassword)
    print(str(encPassword))

    record = appName + ',' + str(encUsername) + ',' + str(encPassword)

    dbfile.write(record)
    dbfile.close()



def decodeDB():
    pass

def userKeyGen():
    userKey = Fernet.generate_key()
    print("New user keys created.")
    #writing keys
    name = input('What do you want your username keyfile to be called? ')
    filename = name + '.key'
    file = open(filename, 'wb')  # Open the file as wb to write bytes
    file.write(userKey)  # The key is type bytes still
    file.close()
    return filename 

def passKeyGen():
    passKey = Fernet.generate_key()
    print("New password key created.")
    #writing keys
    name = input('What do you want your password keyfile to be called? ')
    filename = name + '.key'
    file = open(filename, 'wb')  # Open the file as wb to write bytes
    file.write(passKey)  # The key is type bytes still
    file.close()
    return filename



#---Code---

fileChoice = ''
files = os.listdir() #NEED TO CHECK ABOUT THE DIRECTORY ABOUT USB
fileNames = []
for x in range(0,len(files)):
    if files[x].endswith('.key'):
        fileNames.append(files[x])
    else:
        pass

if len(fileNames) > 2:
    print('Found ', len(fileNames), ' keys.')
    print('There are ', len(fileNames), ' key files ', fileNames,' which one would you like to use for the username (Please choose a number between 1 and ', len(fileNames))
    choiceFile = int(input())
    userFileKey = fileNames[choiceFile-1]
    print('There are ', len(fileNames), ' key files ', fileNames,' which one would you like to use for the password (Please choose a number between 1 and ', len(fileNames))
    choiceFile = int(input())
    passFileKey = fileNames[choiceFile-1]
    
elif len(fileNames) == 0:
    print('No Key Files found')
    keyMake = input('Can you locate the files? (y/n)')
    if keyMake == "y":
        #Add option to find it theirselves
        pass
    elif keyMake == 'n':
        userFileKey = userKeyGen()
        passFileKey = passKeyGen()
        time.sleep(0.3)
        print('Returning to Home...')
        choice()
    else:
        print('Unrecognised input')
elif len(fileNames) == 1:
    print('Only One Key found. 2 Keys Needed to continue')
else:
    print('Found Keys')
    print('Which Key do we use for username encrytion/decryption out of', fileNames, ' (Please choose a number between 1 and ', len(fileNames))
    usernameNumKey = int(input())
    userFileKey = fileNames[usernameNumKey-1]
    if usernameNumKey == 0:
        passFileKey = fileNames[1]
    else:
        passFileKey = fileNames[0]

choice()


