from words import words # To just make sure no other files can access it
import random
import string

'''As some of the words divided by space or - '''
def get_valid_word(words:list):
    word:str = random.choice(words) #choice accepts sequence/iterables

    '''as some words has space or -'''
    while ' ' in word or '-' in word:
        word = random.choice(words) # it keeps on iterating until condition satisfies

    return word.upper() # now it returns only valid words


def run_game():
    word = get_valid_word(words)
    count_mistakes:int = 0
    letters_guess = []
    letter_word = list(word)

    print(f'the word has {len(word)} letters')
    user_input = str(input('Guess the word: '))

    for char in word:
        if user_input == char:
            display_word.index(user_input)
            print(display_word)

        else:
            display_word = len(word) * '_'
            print(display_word)


if __name__ == '__main__':
    run_game()