# Learning Python3 the Hard Way. Excercise 25. Even More Practice.

# Example:
# 'python3' to run python interpreter
# 'from lpthw_ex25 import *' This will import all the functions from this file.

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    print(words[0])
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    print(words[-1])
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
