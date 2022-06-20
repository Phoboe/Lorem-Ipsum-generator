"""
Docstring for main.py :

    This program is used whith a .txt input file named 'LoremIpsum.txt' which is used to output a .csv file contaning all the words of LoremIpsum.txt as a list. the output's file name is 'LoremIpsum.csv'


"""

inputFileName = 'LoremIpsum.txt'
# inputFileName = 'little text.txt' # to test count_next_words function
# inputFileName = 'lultime experience.txt' # french big text
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

        with open(fileName, mode='r', encoding="utf8") as file:
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
    's’',
    'm’',
    'l’',
    'd’',
    'qu’',
    '>',
    '<',
    '...',
    '(',
    ')',
    '{',
    '}',
    '[',
    ']',
    '\\',
    '/',
    '+',
    '$',
    '      ',
    '     ',
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
    state = 0
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

        state += 1
        if state % (len(words)/100) == 0:
            percentage = 100 * (k/len(words))
            print(f'Progression : {round(percentage, 2)}%')
        pass
    print('Progression : 100%. END')


    print('\n')
    print_list(result)
    print('\nScript readable string : ')
    print(result)




    return result

def count_next_words2(words):
    """ Creates a list with all the words and the chance for each word to be written next.
        text is a list of all the words of the text in order """

    parsed_words = remove_duplicates(words)

    result = [] # list of lists containing the couples of words and their probability to be next to another

    columns = ['']
    for word in parsed_words: # set the columns names
        columns.append(word)
    result.append(columns)

    for parsed in parsed_words: # initialising values with 0
        couples = [parsed]
        for word in parsed_words:
            value = 0
            couples.append(value)
            continue
        result.append(couples) # result is now constructed but with empty values

    print(f'\nFinding next words : ')
    state = 0
    for i in range(len(words)-1): # read the text
        word = words[i]
        next = words[i+1]
        for x in range(len(result)):
            current = result[x][0]
            for y in range(len(result[x])):
                if x >= 1: # ignore the first element because its not a couple but the current word
                    if current == word and next == result[0][y]: # found a next word corresponding
                        result[x][y] += 1 # add an occurence for this word
        percentage = int((100 * (i/len(words)))*100)/100

        state += 1
        if state == 10:
            state = 0
            percentage = 100 * (i/len(words))
            print(f'Progression : {round(percentage, 3)}%')
        pass

    print('Progression : 100%. END')


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


print('-'*15, '\nSorted words by lenght :\n')
no_duplicates = sort_by_lenght(remove_duplicates(words))
print_list(no_duplicates)
print(f'\nTotal {len(words)} words in the text with {len(no_duplicates)} diferents words. \n')

import time
start_time = time.time()
probability = count_next_words2(words)
seconds = time.time() - start_time
print(f'\n --- count_next_words() took {seconds} to execute. ---')



export(probability, outputFileName)
