#Filename main.py
#Author: Jake Davis<jake.davis@gmail.com>

#Scope description for this project can be found at: https://github.com/Yankeeland/duplicatePhotoRemover/blob/master/README.md
#===================================

import os
#send2trash

#Load the UI

DEBUG = True


if DEBUG:
    print('Current working directory: ' + os.getcwd())

#Input a directory to scan
#check to make sure that the directory is valid
directoryToScan = 'NOTAPATH'
while not os.path.isdir(os.path.abspath(directoryToScan)):
    directoryToScan = input("Please enter a directory to scan:")

directoryToScan = os.path.abspath(directoryToScan)
os.chdir(directoryToScan)
if DEBUG:
    print('Current working directory: ' + os.getcwd())
if DEBUG:
    print('Directory found is: ' + directoryToScan)
#Scan the directory looking for image files
for filename in os.listdir(directoryToScan):

    #skip directories
    if os.path.isfile(filename):
        if DEBUG: print('Yeah! We have a file called: ' + filename)

    #if the filename is a .jpg, add it to the dictionary

#load all image files into a dictionary with unique atributes for comparing


#scan through each file comparing for duplicates
#when a duplicate is found, present the user with a choice of which to keep, the choice should show the originating directory


#Present duplicates one at a time and ask the user to decide which to keep and which to put into trash




#show all done




#go back to the beginning




