#NOTE
#Different key for Username and password??
#Add option for path to find themselves

import os
from cryptography.fernet import Fernet

def findFiles():
    if len(fileNames) > 1:
        print('Found ', len(fileNames), ' keys.')
        ''' May not need as different key for username and password
        manyFiles = input('There are 2 key files ', fileNames,' which one would you like to use (Please choose a number between 1 and', len(fileNames))
        fileChoice = fileNames[manyFiles]
        '''
    elif len(fileNames) == 0:
        print('No Key Files found')
        #Add option to find it theirselves
    else:
        print('Only One Key found. 2 Keys Needed to continue')

key = Fernet.generate_key()


fileChoice = ''
files = os.listdir() #NEED TO CHECK ABOUT THE DIRECTORY ABOUT USB
fileNames = []
for x in range(0,len(files)):
    if files[x].endswith('.key'):
        fileNames.append(files[x])
    else:
        pass



'''
#writing keys
file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()

#reading keys
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()'''