#NOTE
#Different key for Username and password??
#Add option for path to find themselves

import os
from cryptography.fernet import Fernet
import time

#---Defines---

userFileKey = ''
passFileKey = ''

def choice():
    choice = input('What do you want to do \n * Decode Username and Password (d) \n * Encode username and password (e) \n')
    if choice == 'e':
        encodeDB()
    else:
        decodeDB() 

    
def encodeDB():
    userKey = open(userFileKey, "r")
    userKey.close()
    passKey = open(passFileKey, "r")
    passKey.close()



def decodeDB():
    pass

def keyGen():
    userKey = Fernet.generate_key()
    passKey = Fernet.generate_key()
    print("New keys created.")
    #writing keys
    name = input('What do you want your username keyfile to be called? ')
    filename = name + '.key'
    file = open(filename, 'wb')  # Open the file as wb to write bytes
    file.write(userKey)  # The key is type bytes still
    file.close()
    name = input('What do you want your password keyfile to be called? ')
    filename1 = name + '.key'
    file = open(filename1, 'wb')  # Open the file as wb to write bytes
    file.write(passKey)  # The key is type bytes still
    file.close()
    print('Taking back to home...')
    time.sleep(0.3)
    choice()
    return filename, filename1



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
    print('There are ', len(fileNames), ' key files ', fileNames,' which one would you like to use for the username (Please choose a number between 1 and', len(fileNames))
    choiceFile = int(input())
    userFileKey = fileNames[choiceFile-1]
    print('There are ', len(fileNames), ' key files ', fileNames,' which one would you like to use for the password (Please choose a number between 1 and', len(fileNames))
    choiceFile = int(input())
    passFileKey = fileNames[choiceFile-1]
    
elif len(fileNames) == 0:
    print('No Key Files found')
    keyMake = input('Can you locate the files? (y/n)')
    if keyMake == "y":
        #Add option to find it theirselves
        pass
    else:
        userFileKey = keyGen()[0]
        passFileKey = keyGen()[1]
elif len(fileNames) == 1:
    print('Only One Key found. 2 Keys Needed to continue')
    choice()
else:
    print('Found Keys')
    #need to choose which key is which

choice()





'''
#reading keys
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()'''
