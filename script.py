#NOTE
#Different key for Username and password??
#Add option for path to find themselves

import os
from cryptography.fernet import Fernet
import time

#---Defines---

def choice():
    choice = input('What do you want to do \n * Decode Username and Password (d) \n * Encode username and password (e) \n')
    findKeys()
    if choice == 'e':
        encodeDB()
    else:
        decodeDB() 

def findKeys():
    if len(fileNames) > 1:
        print('Found ', len(fileNames), ' keys.')
        ''' May not need as different key for username and password
        manyFiles = input('There are 2 key files ', fileNames,' which one would you like to use (Please choose a number between 1 and', len(fileNames))
        fileChoice = fileNames[manyFiles]
        '''
    elif len(fileNames) == 0:
        print('No Key Files found')
        keyMake = input('Can you locate the files? (y/n)')
        if keyMake == "y":
            #Add option to find it theirselves
            pass
        else:
            keyGen()
    else:
        print('Only One Key found. 2 Keys Needed to continue')
    
def encodeDB():
    pass

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
    filename = name + '.key'
    file = open(filename, 'wb')  # Open the file as wb to write bytes
    file.write(passKey)  # The key is type bytes still
    file.close()
    print('Taking back to home...')
    time.sleep(0.3)
    choice()



#---Code---

fileChoice = ''
files = os.listdir() #NEED TO CHECK ABOUT THE DIRECTORY ABOUT USB
fileNames = []
for x in range(0,len(files)):
    if files[x].endswith('.key'):
        fileNames.append(files[x])
    else:
        pass

choice()





'''
#reading keys
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()'''
