"""
CSSE1001 Assignment 1
Semester 2, 2020
"""

from a1_support import *
import random

# Fill these in with your details
__author__ = "{{Riley Mosca}} ({{}})"
__email__ = ""
__date__ = "22/08/2020"


def main():
    """
    Handles top-level interaction with user.
    """
    print(WELCOME)
    action = str(input(INPUT_ACTION))
    while True:
        if action == "q":
            return
        elif action == "h":
            print(HELP)
            break
        elif action == "s":
            break
        else:
            print(INVALID)
            while True:
                action = str(input(INPUT_ACTION))
                if action == "q":
                    break
                elif action == "h":
                    print(HELP)
                    break
                elif action == "s":
                    break
                else:
                    break
    while True:
        word_select = str(input("Do you want a 'FIXED' or 'ARBITRARY' length word?: "))
        if word_select == "ARBITRARY" or word_select == "FIXED":
            word = (select_word_at_random(word_select))
            print("\nNow try and guess the word, step by step!!")
            word_length = len(word)
            break
        break


def select_word_at_random(word_select):
    """
    A function that will select a word from either the ARBITRARY or FIXED file
    depending on what the user inputs upon the initialisation of the program.

    parameters:
        word_select (str): either FIXED or ARBITRARY as per user input.

    return:
        str: word chosen from the ARBITRARY or FIXED text files.
    """

    if word_select == "ARBITRARY":
        tuple_arbitrary = load_words("ARBITRARY")
        words = tuple_arbitrary[random.randrange(len(tuple_arbitrary))]
        return words

    if word_select == "FIXED":
        tuple_fixed = load_words("FIXED")
        words = tuple_fixed[random.randrange(len(tuple_fixed))]
        return words


def create_guess_line(guess_no, word_length):
    """
    A function which will create a new guess line allowing the user to guess the next part of the word

    parameters:
        guess_no int(): Guess number which will display in the guess line
        word_length int(): Length of the word that's used in the guessing line

    return:
        str: String containing the new guess line
            Format for guess line
            Guess 1| * | * | * | * | * | * |
    """

    guess_tuple = GUESS_INDEX_TUPLE[word_length -6]
    guess_line = f'Guess {guess_no}' + '|'

    for value in range (word_length):
        if guess_tuple[guess_no -1][0] <= value <= guess_tuple[guess_no -1][1]:
            guess_line += ' * ' + '|'
        else:
            guess_line += ' ' + '-' + ' ' + '|'
    return guess_line




def display_guess_matrix(guess_no, word_length, scores):
    """
    A function which will display the guess game matrix, as per the Assignment format

    parameters:
        guess_no int(): Guess number which will be displayed in the guess line
        word_length int(): Length of the word that's used in the guessing line
        scores (Tuple[int, ...]): A tuple containing the scores of the player for each guess

    return:
        None: This will act as a procedure rather than a function, i.e. a format for the game matrix
    """
    guess_score = 0
    game_line = f'Guess {guess_no}' + word_length * "| - |"
    value = 1
    matrix_line = "       "
    for value in range(value):
        if word_length == 6:
            matrix_line += "| 1 | 2 | 3 | 4 | 5 | 6 |"
            break
        elif word_length == 7:
            matrix_line += "| 1 | 2 | 3 | 4 | 5 | 6 | 7 |"
            break
        elif word_length == 8:
            matrix_line += "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |"
            break
        elif word_length == 9:
            matrix_line += "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |"
            break
        else:
            return
    print(matrix_line + "\n" + 4 * (word_length) * "-" + 9 * "-")
    for i in range(1, guess_no):
        print(create_guess_line(i, word_length) + '   ' + f'{scores[i - 1]} Points')
        print("-" * (9 + 4 * word_length))
    print(create_guess_line(guess_no, word_length))
    print("-" * (9 + 4 * word_length))



def compute_value_for_guess(word, start_index, end_index, guess):
    """
    A function used to calculate the value for the score of the user's guess

    parameters:
        word (str):
        start_index (int):
        end_index (int):
        guess (str):

    return:
        int: Integer value for the user's score with respect to their guess.

    """
    guess_score = 0
    correct_word = word[start_index: end_index + 1]
    for value in range(len(guess)):
        if guess[value] == correct_word[value]:
            if guess[value] in VOWELS:
                guess_score += 14
            else:
                guess_score +=12
        elif guess[value] in correct_word:
            guess_score += 5
    return guess_score




if __name__ == "__main__":
    main()
