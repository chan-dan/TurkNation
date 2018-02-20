'''
Created on Feb 16, 2015

@author: xiaoma
'''


import os
from mhlib import isnumeric

DIR = os.getcwd().replace("\\","/")
IN_FILE = "/Profiles.csv"
OUT_FILE = "/UserIDs.csv"

def main():
    long_string = ""
    with open(DIR+IN_FILE, 'r') as fin:
        for line in fin.readlines():
            if line.strip() == "": # occasionally there is an empty line
                continue
            try:
                #print "\nThis is the result of Split: " + line.split("?")[1].split("-")[0]
                useridTest = line.split("?")[1].split("-")[0]
                usernameTest = line.strip().split("?")[1].split("-",1)[1]
            except:
                print "\nSplit error!"
            if not (useridTest.isdigit()):
                print "\nParse error!"
                continue
            long_string += useridTest + "," + usernameTest + "\n"
    # save long string of userIDs into target file
    with open(DIR+OUT_FILE, 'w') as fin:
        fin.write(long_string)

if __name__ == '__main__':
    main()