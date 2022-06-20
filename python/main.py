"""
Docstring for main.py :

    This program is used whith a .txt input file named 'LoremIpsum.txt' which is used to output a .csv file contaning all the words of LoremIpsum.txt as a list. the output's file name is 'LoremIpsum.csv'


"""

inputFileName = 'LoremIpsum.txt'
# inputFileName = 'little text.txt' # to test count_next_words function
outputFileName = 'LoremIpsum.csv'

import os
import csv

os.system('cls')


def print_list(array):
    for elt in array:
        print(elt)
        continue
    return None




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
    ';',
    '\n',
    '    ',
    '   ',
    '  ',
    ]

    for symbol in symbols:
        string = string.replace(symbol, ' ') # delete all symbols
    string = string.lower()

    words = string.split(' ') # Transform the string into a list
    remove_duplicates(words)
    words.remove('')
    return words

def remove_duplicates(array):
    array = list(dict.fromkeys(array)) # remove all duplicates
    return array

def sort_by_lenght(unsorted_list):
    """ Sort a list by the lenght of its values. Values are lists or strings. """
    sorted_list = sorted(unsorted_list, key=len)
    return sorted_list

def count_next_words(words):
    """ Creates a list with all the words and the chance for each word to be written next.
        text is a list of all the words of the text in order """

    parsed_words = remove_duplicates(words)

    result = [] # list of lists containing the couples of words and their probability to be next to another

    for parsed in parsed_words: # initialising couples of words like (next_word, weight)
        couples = [parsed]
        for word in parsed_words:
            couple = [word, 0]
            couples.append(couple)
            continue
        result.append(couples) # result is now constructed but with empty values

    print(f'Finding next words : ')
    for k in range(len(words)-1): # read the text
        word = words[k]
        next = words[k+1]
        # print(f'{word} -> {next}')
        for i in range(len(result)):
            current = result[i][0]
            # print(f'  Current word : {current}')
            for j in range(len(result[i])):
                if j >= 1: # ignore the first element because its not a couple but the current word
                    couple = result[i][j]
                    # print(f'    {couple}')
                    if current == word and next == couple[0]: # found a next word corresponding
                        # print(f'  Found a corresponding word : {next} is after {current}.')
                        result[i][j][1] += 1 # add an occurence for this word
        percentage = int((100 * (k/len(words)))*100)/100
        # os.system('cls')
        if percentage % 1 == 0.0:
            print(f'Progression : {int(percentage)}%.')



    print('\n')
    print_list(result)
    print('\nScript readable string : ')
    print(result)




    return result


def export(array, fileName):
    with open(fileName, mode='w', newline='') as file:
        writer = csv.writer(file)

        for i in range(len(array)):
            row = array[i]
            writer.writerow(row)
    pass




lines  = get_lorem_ipsum(inputFileName)
string = list_to_string(lines)
words  = get_words(string)

print(f'\nTotal {len(words)} words. \n')

print('-'*15, '\nSorted words by lenght :\n')
print_list(sort_by_lenght(remove_duplicates(words)))

import time
start_time = time.time()
probability = count_next_words(words)
seconds = time.time() - start_time
print(f'\n --- count_next_words() took {seconds} to execute. ---')



export(probability, outputFileName)
