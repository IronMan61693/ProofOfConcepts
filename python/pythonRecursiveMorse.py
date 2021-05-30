#!/usr/bin/env python3

def main():

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

    answer = "101100101111111011"
    test = "11001"

    wordsDict = {}
    morseWordFunc (test, "", 0, morseDict, wordsDict)
    for word in wordsDict:
        print(word)


def morseWordFunc(binString, ansString, binIndex, morseDict, wordsDict):
    length = len(binString)
    if binIndex == len(binString):
        wordsDict[ansString] =1
    if binIndex +3 < len(binString):
        if binString[binIndex:binIndex+4] in morseDict:
            newString = ansString + morseDict[binString[binIndex:binIndex+4]]
            morseWordFunc(binString, newString, binIndex+4, morseDict, wordsDict)
    if binIndex +2 < len(binString):
        if binString[binIndex:binIndex+3] in morseDict:
            newString = ansString + morseDict[binString[binIndex:binIndex+3]]
            morseWordFunc(binString, newString, binIndex+3, morseDict, wordsDict)
    if binIndex +1 < len(binString):
        if binString[binIndex:binIndex+2] in morseDict:
            newString = ansString + morseDict[binString[binIndex:binIndex+2]]
            morseWordFunc(binString, newString, binIndex+2, morseDict, wordsDict)
    if binIndex +0 < len(binString):
        if binString[binIndex:binIndex+1] in morseDict:
            newString = ansString + morseDict[binString[binIndex:binIndex+1]]
            morseWordFunc(binString, newString, binIndex+1, morseDict, wordsDict)

main()
