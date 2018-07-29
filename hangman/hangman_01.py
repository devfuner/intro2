import sys
import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']


def word_preprocess():
    words = []

    with open('words.txt', 'r') as f:
        for line in f.readlines():
            words.append(line.strip('\n'))
    return words


def word_choice(words):
    return random.choice(words)


def end_game(user_input):
    if "Q" == user_input.upper():
        sys.exit(0)


def word_checker(word, user_input_word):
    underline = '_' * len(word)

    for user_input in user_input_word:
        if user_input in word:
            index = word.index(user_input)
            print(index)

            underline = underline[:index] + user_input + underline[index + 1:]
            print(' '.join(underline))


def main(word):
    user_input_word = set()
    word_length = len(word)

    print("_ " * word_length)

    while True:

        user_input = input('>')

        end_game(user_input)

        user_input_word.add(user_input)

        word_checker(word, user_input_word)


if __name__ == '__main__':
    words = word_preprocess()

    word = word_choice(words)
    print(word)

    main(word)


