"""
Docstring for main.py :

    This program is used whith a .txt input file named 'LoremIpsum.txt' which is used to output a .csv file contaning all the words of LoremIpsum.txt as a list. the output's file name is 'LoremIpsum.csv'


"""

inputFileName = 'LoremIpsum.txt'
outputFileName = 'LoremIpsum.csv'

import os
import csv

os.system('cls')







def get_lorem_ipsum(fileName):
    """ get all lines of the file and output a list. """

    try: # If the file already exists

        with open(fileName, mode='r') as file:
            array = file.readlines()

    except FileNotFoundError:

        print(f'\nThe file \"{fileName}\" does not exists. \nPlease add a file contaning a Lorem Ipsum text source.')
        exit()

    return array

def list_to_string(array):

    string = ''
    for elt in array:
        string += elt

    return string

def get_words(string):
    """ Transform a string into a list of all the words with lower case and no symbol. """

    symbols = [
    '.',
    ',',
    '\n',
    '    ',
    '   ',
    '  ',
    ]

    for symbol in symbols:
        string = string.replace(symbol, ' ') # delete all symbols
    string = string.lower()

    words = string.split(' ') # Transform the string into a list
    words = list(dict.fromkeys(words)) # remove all duplicates
    words.remove('')

    return words

def export(array, fileName):
    with open(fileName, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['words : '])
        for row in array:
            writer.writerow([row])
    pass




lines = get_lorem_ipsum(inputFileName)
string = list_to_string(lines)
words = get_words(string)


for word in words:
    print(word)

print(f'Total {len(words)} words. \n')

print(words)


export(words, outputFileName)
