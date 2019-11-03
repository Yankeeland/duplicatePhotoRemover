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
masterDirectory = 'NOTAPATH'

while not os.path.isdir(os.path.abspath(directoryToScan)):
    directoryToScan = input("Please enter a directory to scan:")
directoryToScan = os.path.abspath(directoryToScan)
os.chdir(directoryToScan)
if DEBUG:
    print('Current working directory: ' + os.getcwd())
if DEBUG:
    print('Directory found is: ' + directoryToScan)

#Input the master directory
while not os.path.isdir(os.path.abspath(masterDirectory)):
    masterDirectory = input("Please enter a directory that contains your master copies:")
masterDirectory = os.path.abspath(masterDirectory)
if DEBUG:
    print('Current working directory: ' + os.getcwd())
if DEBUG:
    print('Master directory found is: ' + masterDirectory)


#initialize the dictionary of pics to compare
picList = {} #originals dictionary
dupPicList = {} #duplicates dictionary

#Scan the directory looking for image files
#Need to change this to walk the directory, otherwise it is not possible to find duplicates
for filename in os.listdir(directoryToScan):

    #skip directories
    if os.path.isfile(filename):
        if DEBUG: print('Yeah! We have a file called: ' + filename)

    #if the filename is a .jpg, add it to the dictionary
        if '.jpg' in filename:
            picName = os.path.basename(filename)
            picPath = os.path.dirname(filename)
            picSize = os.path.getsize(filename)
            if picName not in picList.keys():
                picList[picName] = [picPath,picSize]
                if DEBUG: print('PICLIST: Added picture ' + picName + ' with size of ' + str(picSize))
            #else: #add to the duplicates dictionary
                #dupPicList[picName] = [picPath,picSize]
                #if DEBUG: print('DUPPICLISTAdded picture ' + picName + ' with size of ' + str(picSize))

#load the master directory

#scan through each file comparing the scanned directory to the master directory

#when a duplicate is found, present the user with a choice of which to keep, the choice should show the originating directory


#Present duplicates one at a time and ask the user to decide which to keep and which to put into trash




#show all done




#go back to the beginning




