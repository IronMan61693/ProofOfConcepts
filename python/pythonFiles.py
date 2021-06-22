#!/usr/bin/env python3

import sys
import os.path
from os import remove
import re


def helpCall():
    print(
        "First ensure you follow the format ./pythonFiles.py test.txt for standard read write behavior\n\n",
        "To modify use ./pythonFiles.py -m fileModified.txt replaceThis withThis  \nif replaceThis is not found,",
        " there won't be any change.\n\n",
        "Use the -a to append with the following format ./pythonFiles.py -a appendMe.txt appendThisWord\n\n",
        "Use the -r to remove the requested fil ./pythonFiles.py -r deleteThis.txt\n",
        "Use -s to see the size of the requested file ./pythonFiles.py -s howBig.txt\n\n",
        "Use -i to insert you word into the middle of the document, \n",
        "if there are no words, we will append your word instead. \n",
        "Use the format ./pythonFiles.py -i insertMe.txt insertThisWord\n",
        "Use -f to find the position of the requested word\n",
        "./pythonFiles.py -f findMe.txt findThisString\n",
    )


def trueFile(argList, tst):
    textDoc = [argument for argument in argList if ".txt" in argument]
    if tst == 0:
        try:
            if os.path.isfile(textDoc[0]):
                return True
        except:
            return False
    else:
        return textDoc[0]


def fileCheck():
    if len(sys.argv) < 2:
        print(
            "This script needs at least 2 arguments, that is just put either --help/-h",
            " for additional options or the file name you want worked with. You input",
            " ",
            len(sys.argv),
            " arguments.",
        )

        sys.exit(-1)
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        helpCall()
        sys.exit(0)
    elif "-a" in sys.argv:
        return "3"

    if not (trueFile(sys.argv, 0)):
        # os.path.isfile(sys.argv[1])
        print(
            "Hey so this function works by opening an existing .txt file, please ensure",
            " we can access the file path and file you input because it appears we can't",
        )

        sys.exit(-1)

    if "-m" in sys.argv:
        return "2"

    elif "-r" in sys.argv:
        youSure = input(
            "You have input the remove flag, are you sure you want to remove"
            + trueFile(sys.argv, 1)
            + "?\n If so Y for yes anything else to close "
        )

        if youSure == "Y":
            return "4"
    elif "-s" in sys.argv:
        return "5"
    elif "-i" in sys.argv:
        return "6"
    elif "-f" in sys.argv:
        return "7"
    return "1"


def getWords(text):
    words = re.findall(r"[a-zA-Z'-]+", text)
    return words


def countWords(aDict, theWord):
    if theWord in aDict:
        count = aDict[theWord]
        aDict[theWord] = count + 1
    else:
        aDict[theWord] = 1


def findDoc():
    if len(sys.argv) != 4:
        print(
            "Hey I need exactly 4 arguments for find functionality\n",
            " like this ./pythonFiles.py -f findMe.txt findThisWord",
        )
        sys.exit(-1)
    textFile = trueFile(sys.argv, 1)
    with open(textFile, mode="r") as READ_FILE:
        myFile = READ_FILE.read()
    READ_FILE.close()
    nowWords = getWords(myFile)
    indices = [index for index, word in enumerate(nowWords) if word == sys.argv[3]]
    print("Your string was found as the following positions:")
    for position in indices:
        relPosition = position
        print(str(relPosition))


def insertDoc():
    if len(sys.argv) != 4:
        print(
            "Hey I need exactly 4 arguments for insert functionality\n",
            " like this ./pythonFiles.py -i insertMe.txt insertThisWord",
        )
        sys.exit(-1)
    textFile = trueFile(sys.argv, 1)
    with open(textFile, mode="r") as READ_FILE:
        myFile = READ_FILE.read()
    READ_FILE.close()
    nowWords = getWords(myFile)
    midPoint = round(len(nowWords) // 2)
    # print(str(len(myFile)))
    nowWords.insert(midPoint, sys.argv[3])
    # if len(nowWords) > 2:
    #
    # elif len(nowWords) < 1:

    with open(textFile, mode="w") as WRITE_FILE:
        for word in nowWords:
            WRITE_FILE.write(word + " ")
    WRITE_FILE.close()


def sizeDoc():
    sizeInBytes = os.path.getsize(trueFile(sys.argv, 1))
    print("The document is ", str(sizeInBytes), " bytes large")


def removeDoc():
    os.remove(trueFile(sys.argv, 1))
    print("File removed")


def appendDoc():
    if len(sys.argv) != 4:
        print(
            "Hey I need exactly 4 arguments for append functionality\n",
            " like this ./pythonFiles.py -a appendMe.txt appendThisWord",
        )
        sys.exit(-1)
    with open(trueFile(sys.argv, 1), mode="a+") as APPEND_FILE:
        print(sys.argv[3])
        APPEND_FILE.write(" " + sys.argv[3])
    APPEND_FILE.close()
    return


def modifyDoc():
    if len(sys.argv) != 5:
        print(
            "Hey I need exactly 5 arguments for the modify functionality\n",
            " like this remember ./pythonFiles.py -m fileModified.txt replaceThis withThis",
        )
        sys.exit(-1)
    textFile = trueFile(sys.argv, 1)
    with open(textFile, mode="r") as READ_FILE:
        checkFile = READ_FILE.read().replace(sys.argv[3], sys.argv[4])
    READ_FILE.close()
    with open(textFile, mode="w") as MODIFY_FILE:
        MODIFY_FILE.write(checkFile)
    MODIFY_FILE.close()
    return


def readAndWrite():
    textFile = trueFile(sys.argv, 1)
    with open(textFile, mode="r") as READ_FILE:
        myFile = READ_FILE.read()
    READ_FILE.close()
    nowWords = getWords(myFile)
    wordDict = {}
    for word in nowWords:
        # print(word)
        countWords(wordDict, word)
    dictItems = wordDict.items()
    sortedWords = sorted(dictItems)
    # print(sortedWords)
    with open("overWritten.txt", mode="w") as WRITE_FILE:
        for wordObj in sortedWords:
            WRITE_FILE.write(wordObj[0] + " is seen: " + str(wordObj[1]) + " times\n")
    WRITE_FILE.close()
    with open("overWritten.txt", mode="r") as OUTPUT_FILE:
        print(OUTPUT_FILE.read())
    OUTPUT_FILE.close()


def main():
    behavior = fileCheck()
    if behavior == "1":
        readAndWrite()
    elif behavior == "2":
        modifyDoc()
    elif behavior == "3":
        appendDoc()
    elif behavior == "4":
        removeDoc()
    elif behavior == "5":
        sizeDoc()
    elif behavior == "6":
        insertDoc()
    elif behavior == "7":
        findDoc()


if __name__ == "__main__":
    main()
