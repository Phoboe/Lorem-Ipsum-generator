"""
Docstring for main.py :

    This program is used whith a .txt input file named 'LoremIpsum.txt' which is used to output a .csv file contaning all the words of LoremIpsum.txt as a list. the output's file name is 'LoremIpsum.csv'


"""

inputFileName = 'LoremIpsum.txt'
outputFileName = 'LoremIpsum.csv'

import os

os.system('cls')







def get_lorem_ipsum(fileName):
    """ get all lines of the file and output a list. """

    try: # If the file already exists

        with open(fileName, encoding='utf-8') as file:
            list = file.readlines()

    except FileNotFoundError:

        print(f'\nThe file \"{fileName}\" does not exists. \nPlease add a file contaning a Lorem Ipsum text source.')
        exit()

    return list

list = get_lorem_ipsum(inputFileName)

sentences = []
for paragraph in list:
    sentences.append(paragraph.split('.'))




for elt in sentences:
    print(elt)
