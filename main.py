#Filename main.py
#Author: Jake Davis<jake.davis@gmail.com>

#Scope description for this project can be found at: https://github.com/Yankeeland/duplicatePhotoRemover/blob/master/README.md
#===================================

import os
#send2trash

#Load the UI

DEBUG = True
#loading testing directories REMOTE THESE 2 LINES WHEN FINISHED
test_path = "C:\\Users\\yanke\\OneDrive\\Documents2\\GitHub\\duplicatePhotoRemover\\photos"
test_master = "C:\\Users\\yanke\\OneDrive\\Documents2\\GitHub\\duplicatePhotoRemover\\masters"

#START OF FUNCTION DEFINITION==========================================================================

#Need to change this to walk the directory, otherwise it is not possible to find duplicates
def scanDir(directoryName):
    picDict = {}
    os.chdir(directoryName)
    for filename in os.listdir(directoryName):
        filename = os.path.abspath(filename)

        # skip directories
        if os.path.isfile(filename):
            # if DEBUG: print('Yeah! We have a file called: ' + filename)

            # if the filename is a .jpg, add it to the dictionary
            if '.jpg' in filename:
                picName = os.path.basename(filename)
                picPath = os.path.dirname(filename)
                picSize = os.path.getsize(filename)
                if picName not in picDict.keys():
                    picDict[picName] = [picPath, picSize]
                    if DEBUG: print('PICDICT: Added picture ' + picName + ' with size of ' + str(picSize) + 'at directory ' + picPath)
    return picDict

#END OF FUNCTION DEFINITION==========================================================================

if DEBUG:
    print('Current working directory: ' + os.getcwd())

#Input a directory to scan
#check to make sure that the directory is valid
directoryToScan = 'NOTAPATH'
masterDirectory = 'NOTAPATH'

while not os.path.isdir(os.path.abspath(directoryToScan)): #while the input is not a directory, keep asking
    #directoryToScan = input("Please enter a directory to scan:")
    directoryToScan = test_path #loading testing directories REMOVE THIS LINE WHEN FINISHED
directoryToScan = os.path.abspath(directoryToScan) #make sure you get the absolute path

if DEBUG:
    print('Directory found is: ' + directoryToScan)

#Input the master directory
while not os.path.isdir(os.path.abspath(masterDirectory)):
    #masterDirectory = input("Please enter a directory that contains your master copies:")
    masterDirectory = test_master #loading testing directories REMOVE THIS LINE WHEN FINISHED
masterDirectory = os.path.abspath(masterDirectory)

if DEBUG:
    print('Master directory found is: ' + masterDirectory)


#load the directories
picList = scanDir(directoryToScan)
masterList = scanDir(masterDirectory)

#scan through each file comparing the scanned directory to the master directory
for picName in picList.keys():
    if picName in masterList.keys():
        if DEBUG: print("HOLY SMOKES! " + str(picList[picName][1]) + " " + str(masterList[picName][1]) )
        #check to see if they are the same size
        if picList[picName][1] == masterList[picName][1]:
            print("Found a duplicate by the name of " + picName)
            print("Which copy would you like to keep? (Choose an Number)")
            choice = 0
            done = False
            while (not done):
                print("1)" + picList[picName][0] + "\\" + picName)
                print("2)" + masterList[picName][0] + "\\" + picName)
                print("3) Skip")
                choice = input()
                if choice == '1':
                    #add new picture to master file under the dir structure
                    done = True
                elif choice == '2':
                    #delete the new picture (send to trash)
                    done = True
                elif choice == '3':
                    # do nothing
                    done = True
                else:
                    continue


#when a duplicate is found, present the user with a choice of which to keep, the choice should show the originating directory


#Present duplicates one at a time and ask the user to decide which to keep and which to put into trash




#show all done




#go back to the beginning




