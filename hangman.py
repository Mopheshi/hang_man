import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have ", lives, " lives left and you have used these letters", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter\n").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print(user_letter + " is not in word")
        elif user_letter in used_letters:
            print("You have already used that letter, try again.")
        else:
            print("You typed an invalid letter, try again.")
    if lives == 0:
        print("You just died, mumu :)!!!, the correct word was ", word)
    else:
        print("You have guessed the word: ", word, " correctly.")


if __name__ == "__main__":
    hangman()