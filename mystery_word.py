import re


def read_file(textfile):
    """Given word file, reads file and returns list of words"""
    text_to_open = open(textfile)
    word_list = text_to_open.readlines()
    text_to_open.close()
    print(type(word_list))
    index = 0
    for word in word_list:
        # take the /n off the end of the string for each word and replace it in word_list
        cleaned_word = word[0:(len(word)-1)]
        word_list[index] = cleaned_word
        index += 1
    print(word_list[0:9])
    print("length of word_list is {}".format(len(word_list)))
    return word_list


def mode_selector():
    """Asks user to select easy (4-6chars), normal(6-8) or hard(8+) mode and returns mode name"""
    user_mode = 0
    while user_mode == 0:
        user_selection = input("Welcome to Mystery Word!\n Do you want to play in (E)ASY, (N)ORMAL, or (H)ARD mode? > ")
        if user_selection.lower() == "e"  or user_selection.lower() == "easy":
            user_mode = "easy"
        elif user_selection.lower() == "n" or user_selection.lower() == "normal":
            user_mode = "normal"
        elif user_selection.lower() == "h" or user_selection.lower() == "hard":
            user_mode = "hard"
        else:
            user_mode = 0
    return user_mode


def easy_words(word_list):
    pass


def medium_words(word_list):
    pass


def hard_words(word_list):
    pass


def random_word(word_list):
    pass


def display_word(word, lst):
    #the blank is default
    pass


def is_word_complete(word, lst):
    pass


if __name__ == "__main__":
    word_list = read_file("web2")
    print(word_list[0:7])
    print(mode_selector())
    # pass