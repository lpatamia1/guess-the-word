import random
import string

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
word_bank = ['python', 'coffee', 'planet', 'window', 'garden', 'music', 'puzzle', 'forest', 'rocket', 'island']
word = random.choice(word_bank)

guessedWord = ['_'] * len(word)
attempts = 6
guessed_letters = set()

# Game Loop
while attempts > 0:
    print(hangman_stages[6 - attempts])
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in guessed_letters:
        print('You already guessed that letter. Try a new one!')
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations! You guessed the word: ' + word)
        break
if attempts == 0 and '_' in guessedWord:
    print(hangman_stages[-1])
    print('\nYou\'ve run out of attempts! The word was: ' + word)