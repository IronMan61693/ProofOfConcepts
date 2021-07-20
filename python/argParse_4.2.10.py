#!/usr/bin/env python3

import argparse
import json
import os.path


myParser = \
 argparse.ArgumentParser(description= ('Interact with a JSON; with no'\
                                       ' argument just verifies json file type.\n'))

helpString = ("Prints True or False dependent on if the specific key"\
             " is in the JSON.\n argParse.py -k key json.json")
myParser.add_argument('-k',
                      '--key',
                      action = 'store',
                      help = helpString)

myParser.add_argument('-i',
                      '--iterate',
                      action = 'store_true',
                      help = 'Iterates over the entire json')

myParser.add_argument('jsonFile',
                      type = str,
                      help = "The JSON file to open")

args = myParser.parse_args()

def iterateJson(jsonData):
    for iterable in jsonData:
        print(iterable)


def main():
    print("Hello World")
    if os.path.isfile(args.jsonFile) and args.jsonFile.endswith('.json'):
        print('Good the file exists and appears to be a json')
        file = open(args.jsonFile)
        jsonData = json.load(file)
        file.close()
    else:
        print("The json doesn't seem to exist")
        return
    if (args.iterate):
        iterateJson(jsonData)

    # print(args.jsonFile)


if (__name__ == "__main__"):
	main()
