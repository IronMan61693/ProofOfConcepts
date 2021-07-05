#!/usr/bin/env python3


class multiReturns:
    def __init__(self, words={}, count=0):
        # I am using a class to return and hold multiple returns, it will hold
        #  the dict of all potential words, and a count of how many
        #  words were found
        self.potentialWords = words
        self.wordCount = count

    def setWords(self, words):
        self.potentialWords = words

    def setCount(self, count):
        self.wordCount = count

    def displayWords(self):
        for word in self.potentialWords:
            print(word)


def userInputFunc():
    requestString = (
        "Please type 1 if you would like to enter your own morse code in 1 0 \n"
        "and 2 if default behavior \n"
    )

    userInput = input(requestString)

    try:
        userInputInt = int(userInput)

    except:
        print("Ah seems your input can't even be an integer")
        exit()

    if not (userInputInt == 1 or userInputInt == 2):
        print(userInput)
        print("The function is exiting because you did not input 1 or 2")
        exit()
    return userInputInt


def recurseiveFunc(morseCode):
    multiReturnInstance = multiReturns()
    morseDict = {}
    morseDict["10"] = "A"
    morseDict["011"] = "B"
    morseDict["0101"] = "C"
    morseDict["011"] = "D"
    morseDict["1"] = "E"
    morseDict["1101"] = "F"
    morseDict["001"] = "G"
    morseDict["1111"] = "H"
    morseDict["11"] = "I"
    morseDict["1000"] = "J"
    morseDict["010"] = "K"
    morseDict["1011"] = "L"
    morseDict["00"] = "M"
    morseDict["01"] = "N"
    morseDict["000"] = "O"
    morseDict["1001"] = "P"
    morseDict["0010"] = "Q"
    morseDict["101"] = "R"
    morseDict["111"] = "S"
    morseDict["0"] = "T"
    morseDict["110"] = "U"
    morseDict["1110"] = "V"
    morseDict["100"] = "W"
    morseDict["0110"] = "X"
    morseDict["0100"] = "Y"
    morseDict["0011"] = "Z"

    # test = "11001"
    # answer = "101100101111111011"
    wordsDict = {}
    morseWordFunc(morseCode, "", 0, morseDict, wordsDict)
    multiReturnInstance.setWords(wordsDict)
    multiReturnInstance.setCount(len(wordsDict))

    return multiReturnInstance


def morseWordFunc(binString, ansString, binIndex, morseDict, wordsDict):
    # in 4.2.5 calling a resursive function
    length = len(binString)
    if binIndex == len(binString):
        wordsDict[ansString] = 1
    if binIndex + 3 < len(binString):
        if binString[binIndex : binIndex + 4] in morseDict:
            newString = ansString + morseDict[binString[binIndex : binIndex + 4]]
            morseWordFunc(binString, newString, binIndex + 4, morseDict, wordsDict)
    if binIndex + 2 < len(binString):
        if binString[binIndex : binIndex + 3] in morseDict:
            newString = ansString + morseDict[binString[binIndex : binIndex + 3]]
            morseWordFunc(binString, newString, binIndex + 3, morseDict, wordsDict)
    if binIndex + 1 < len(binString):
        if binString[binIndex : binIndex + 2] in morseDict:
            newString = ansString + morseDict[binString[binIndex : binIndex + 2]]
            morseWordFunc(binString, newString, binIndex + 2, morseDict, wordsDict)
    if binIndex + 0 < len(binString):
        if binString[binIndex : binIndex + 1] in morseDict:
            newString = ansString + morseDict[binString[binIndex : binIndex + 1]]
            morseWordFunc(binString, newString, binIndex + 1, morseDict, wordsDict)


def main():
    userChoice = userInputFunc()
    if userChoice == 2:
        multipleReturnedValues = recurseiveFunc("11001")
    elif userChoice == 1:
        promptString = (
            "Ah you have chosen to enter your own morse."
            " Well, luckily for you, you can enter it in binary where 1 is"
            " a dot, and 0 is a dash, or just enter an integer and it will"
            " be forced to binary.\n"
        )
        morseChoice = input(promptString)
        try:
            morseInt = int(morseChoice)
        except:
            print(
                "Ah seems you did not enter something that can be an int, this could be"
                " a while loop, but just exiting"
            )
            exit()
    multipleReturnedValues = recurseiveFunc(bin(morseInt)[2:])
    print("Here are the words you asked for:")
    multipleReturnedValues.displayWords()
    print(
        "The number of unique words from the input is {}".format(
            multipleReturnedValues.wordCount
        )
    )


if __name__ == "__main__":
    main()
