import re
import random


def read_file(textfile):
    """Given word file, reads file and returns list of words"""
    text_to_open = open(textfile)
    word_list = text_to_open.readlines()
    text_to_open.close()
    print(type(word_list))
    index = 0
    for word in word_list:
        # take the /n off the end of the string for each word and replace it in word_list
        cleaned_word = word[0:(len(word) - 1)]
        word_list[index] = cleaned_word
        index += 1
    print(word_list[0:9])
    print("length of word_list is {}".format(len(word_list)))
    return word_list


def size_selector():
    """Asks user to select easy (4-6), normal(6-8) or hard(8+) mode and returns randomized number of chars"""
    user_mode = 0
    while user_mode == 0:
        user_selection = input("Welcome to Mystery Word!\n Do you want to play in (E)ASY, (N)ORMAL, or (H)ARD mode? > ")
        if user_selection.lower() == "e" or user_selection.lower() == "easy":
            user_mode = "easy"
            easy_words(word_list)
        elif user_selection.lower() == "n" or user_selection.lower() == "normal":
            medium_words(word_list)
            user_mode = "normal"
        elif user_selection.lower() == "h" or user_selection.lower() == "hard":
            hard_words(word_list)
            user_mode = "hard"
        else:
            user_mode = 0
    return user_mode


def easy_words(word_list):
    """Given word list, returns a subset list of those words 4-6 characters in size"""
    # char_size = random.randrange(4, (6+1), 1)
    mini_word_list = []
    for word in word_list:
        if 4 <= len(word) <= 6:
            mini_word_list.append(word)
    return mini_word_list


def medium_words(word_list):
    """Given word list, returns a subset list of those words 6-8 characters in size"""
    mini_word_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 8:
            mini_word_list.append(word)
    return mini_word_list


def hard_words(word_list):
    """Given word list, returns a subset list of those words 8 or more characters in size"""
    mini_word_list = []
    for word in word_list:
        if len(word) >= 8:
            mini_word_list.append(word)
    return mini_word_list


def ask_user_guess(mini_word_list):
    magic_word = random_word(word_list)
    guesses_left = 8
    char_length = len(mini_word_list[0])
    print("I'm thinking of a word that has {} characters.".format(char_length))
    print("_ " * char_length)
    while guesses_left > 0:
        user_guess = input("Spell the word. Give me a letter > ")
        if user_guess in magic_word:
            print("Yes {} is in {}".format(user_guess, magic_word))
        else:
            print("There is no {} in the mystery word.".format(user_guess))
            guesses_left -= 1

def random_word(word_list):
    """This picks a random word from our word_list just to pass test"""
    return (random.sample(word_list, 1))[0]
    #return random.sample(word_list, 1)


def display_word(word, lst):
    # the blank is default
    pass


def is_word_complete(word, lst):
    pass


if __name__ == "__main__":
    word_list = read_file("web2")
    print(word_list[0:7])
    print(size_selector())
    ask_user_guess(easy_words(word_list))
