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

def easy_words(word_list):
    pass


def medium_words(word_list):
    pass


def hard_words(word_list):
    pass


def random_word(word_list):
    pass


def display_word(word, lst):
    pass


def is_word_complete(word, lst):
    pass


if __name__ == "__main__":
    print(read_file("web2"))
    # pass