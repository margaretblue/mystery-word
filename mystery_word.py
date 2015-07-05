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
    print("length of word_list is {}".format(len(word_list)))
    return word_list


def size_selector(word_list):
    """Asks user to select easy (4-6), normal(6-8) or hard(8+), runs mode funtion, returns mini_word_list"""
    user_mode = 0
    while user_mode == 0:
        user_selection = input("Welcome to Mystery Word\n  (E)ASY, (N)ORMAL, or (H)ARD mode? \n> ")
        if user_selection.lower() == "e" or user_selection.lower() == "easy":
            print("Easy Mode Enabled")
            user_mode = "easy"
            mini_word_list = easy_words(word_list)
            return mini_word_list
        elif user_selection.lower() == "n" or user_selection.lower() == "normal":
            print("Normal Mode Enabled")
            user_mode = "normal"
            mini_word_list = medium_words(word_list)
            return mini_word_list
        elif user_selection.lower() == "h" or user_selection.lower() == "hard":
            print("Hard Mode Enabled")
            mini_word_list = hard_words(word_list)
            user_mode = "hard"
            return mini_word_list
        else:
            user_mode = 0


def easy_words(word_list):
    """Given word list, returns a subset list of those words 4-6 characters in size"""
    print("Easy Peasy")
    print(word_list[0])
    mini_word_list = []
    for word in word_list:
        if 4 <= len(word) <= 6:
            mini_word_list.append(word)
    print("{} possible words".format(len(mini_word_list)))
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
    """Given mini_word list, prompts user to guess letters, if match game won. also launches is_play_again()"""
    magic_word = ''.join((random_word(mini_word_list)).upper())
    guesses_left = 8
    char_length = len(magic_word)
    print("I'm thinking of a word that has {} characters.".format(char_length))
    guessed_word = str("_" * char_length)
    while guessed_word != magic_word and guesses_left > 0:
        user_guess = (input("Give me a letter \n> ")).upper()
        if user_guess in magic_word:
            index = 0
            for letter in magic_word:
                # if magic word letter at that index matches letter of user_guess, replace guessed_word at that index
                if magic_word[index] == user_guess:
                    list_guessed_word = list(guessed_word)
                    list_guessed_word[index] = user_guess
                    guessed_word = ''.join(list_guessed_word)
                index += 1
            # TODO call a funciton display_word() that properly spaces words
            print("Yes {} is in the Mystery Word DEBUG:{}".format(user_guess, magic_word))
            print(display_word(guessed_word))
        else:
            print("There is no {} in the mystery word DEBUG: {}.".format(user_guess, magic_word))
            print(display_word(guessed_word))
            guesses_left -= 1
    if guessed_word == magic_word:
        print("Congratulations! The Mystery Word is {}".format(guessed_word))
        is_play_again()
    else:
        print("Time out. The Mystery word was {}".format(magic_word))
        is_play_again()


def is_play_again():
    """Prompts user to replay, if so relaunches gameplay"""
    play_status = input("Would you like to play again? Y or N >\n ")
    if play_status.upper() == "Y":
        mini_word_list = (size_selector(word_list))
        ask_user_guess(mini_word_list)
    else:
        print("Bye, thank you for playing.")


def random_word(word_list):
    """This picks a random word from our word_list just to pass test"""
    return (random.sample(word_list, 1))[0]


def display_word(word):
    """Takes in a string, returns that string single-spaced"""
    return ' '.join(list(word))


def is_word_complete(word, lst):
    pass


if __name__ == "__main__":
    word_list = read_file("web2")
    ask_user_guess(size_selector(word_list))
    # mini_word_list = (size_selector(word_list))
    # ask_user_guess(mini_word_list)
