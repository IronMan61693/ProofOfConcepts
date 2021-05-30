#!/usr/bin/env python3
import sys

def parseFunction():
    list_of_args = sys.argv
    intArray = []
    strArray = []
    print(len(list_of_args), " arguments passed")
    if len(list_of_args) <= 2:
        print("Please input at least an integer and string to demonstrate")

    for helpCheck in list_of_args:
        if helpCheck == "--help" or helpCheck == "-h":
            print("This goes through any arguments you have added in the command"
            ," line and sorts them into integers and everything else and prints those"
            ," as lists, so there really isn't bad input. Have fun!")
            return ("", "")

    for argument in list_of_args:
        # Here we will make an array of all the integers and one of everything else
        try:
            intArg = int(argument)
            intArray.append(intArg)
        except:
            strArray.append(argument)
    return intArray, strArray

# This is now an array of the arguments passed on the commandline

# I hope the library in python counts as built-in functionality
def main():
    parseTup = parseFunction()
    intArray = parseTup[0]
    strArray = parseTup[1]
    print("ints")
    for intExample in intArray:
        print(intExample)
    print("strings")
    for strExample in strArray:
        print(strExample)


main()
