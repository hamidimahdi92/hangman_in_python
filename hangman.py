from words import words
import random
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  # what letters user has guessed

    def full_message():
        print(f'Yaaay, you guessed the {word} right')

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) => 'a b cd'
        print('You have', lives, 'lives left and used these letters: ', ' '.join(used_letters))

        # What current word is: i.e W _ R D
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list), '\n')

        user_letter = input('Guess a letter: \n')
        if user_letter == word:
            # print('Yaaay you guessed it right')
            return full_message()
        elif user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # increase one lives if user guessed a letter
                print('Letter is not in word!')

        elif user_letter in used_letters:
            print('You have already used that character. Please choose another letter')
        else:
            print('You entered an invalid character. Try again!')
    # gets here until len(word_letters) == 0
    if lives == 0:
        print('You died, sorry the word was', word, '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
    else:
        print('Whoooa, you guessed the word', word, ' !!')


hangman()
