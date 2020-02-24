import csv
import os
import re

def loopy():
    with open(writefile,"w") as outputfile: #writing
        for i in range(number):
            current = folders[i]
            os.chdir(mainfolder + "messages/" + current)
            print("Reading Folder:" + current)
            with open('messages.csv', errors='ignore') as inputfile: #reading, also ignores unicode errors since i may have spammed ascii shit a long time ago
                inputmessages = csv.reader(inputfile)
                inputfile.readline() #skips the first line
                for section in inputmessages:
                    validwords = re.sub(combinedpattern , '', section[2]).strip() #takes out links and strips whitespace
                    if not validwords: #checks if string is blank and skips it
                        pass
                    else:
                        outputfile.write(str(validwords) + "\n") #writes the read messages to the write file
            os.chdir("..")#backs out to parent folder


folders = os.listdir('messages') #list of folders
number = len(folders) #number of folders

mainfolder = "PATH TO FOLDER" #set this to the path to the main folder that contains the messages folder
filename = "NAME OF FILE .txt" #name of the output txt file
writefile = mainfolder + filename #full output file path


#regex shit
pattern1 = r'http\S+' #links
pattern2 = r'(:|<:|<a:)((\w{1,64}:\d{17,18})|(\w{1,64}))(:|>)' #emojis
pattern3 = r'<[@#][!&]?[0-9]+>'
combinedpattern = r'|'.join((pattern1, pattern2, pattern3))

loopy()