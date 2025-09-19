import random
import string

from colorama import Fore, Style, init
init(autoreset=True)

hangman_stages = [
'''
               +---+
               |   |
                   |
                   |
                   |
                   |
             =========''',
            '''
               +---+
               |   |
               O   |
                   |
                   |
                   |
             =========''',
            '''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
             =========''',
            '''
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
             =========''',
            '''
               +---+
               |   |
               O   |
              /|\\  |
                   |
                   |
             =========''',
            '''
               +---+
               |   |
               O   |
              /|\\  |
              /    |
                   |
             =========''',
            '''
               +---+
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
             ========='''
]
word_bank = ['python', 'coffee', 'planet', 'window', 'garden', 'music', 'puzzle', 'forest', 'rocket', 'island', 'button', 'candle', 'matcha', 'anime', 'japan', 'karaoke', 'zombie']
def play_game():
    word = random.choice(word_bank)
    guessedWord = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print(Fore.YELLOW + "Welcome to Hangman! Guess the word, one letter at a time.")
    print(Fore.YELLOW + "Don't repeat guesses. Good luck!\n")
    
    # Game Loop
    while attempts > 0:
        print(Fore.YELLOW + hangman_stages[6 - attempts])
        print(Fore.CYAN + '\nCurrent word: ' + ' '.join(guessedWord))
        print(Fore.MAGENTA + 'Guessed letters: ' + ', '.join(sorted(guessed_letters)))
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter. Try a new one!')
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWord[i] = guess
            print(Fore.GREEN + 'Great guess!')
        else:
            attempts -= 1
            print(Fore.RED + 'Wrong guess! Attempts left: ' + str(attempts))
        if '_' not in guessedWord:
            print('\nCongratulations! You guessed the word: ' + word)
            break
        if attempts == 0 and '_' in guessedWord:
            print(hangman_stages[-1])
            print('\nYou\'ve run out of attempts! The word was: ' + word)
while True:
    play_game()
    again = input(Fore.YELLOW + '\nPlay again? (y/n): ').lower()
    if again != 'y':
        print(Fore.CYAN + 'Thanks for playing!')
        break