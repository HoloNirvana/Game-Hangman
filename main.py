# The Hangman game
# Under the influence of "100 Days of Code - The Complete Python Pro Bootcamp for 2021" on udemy.com website

import random
import hangman_words
import hangman_art

# The player chooses the level of difficulty
dif_level = int(input("chose difficulty level (3 to 10): "))

# Selection of words according to the level of difficulty
word_list = hangman_words.word_list
word_list_with_dif = []
for i in range(len(word_list)):
    if len(word_list[i]) == dif_level:
        word_list_with_dif.append(word_list[i])

# Random word selecion
chosen_word = list(random.choice(word_list_with_dif))

# Game parameters setting
current_variant = []
for letter in chosen_word:
    current_variant += "_"
lives_left = 6
we_are_in_game = True

# Printing Logo & starting position
print(hangman_art.logo)
print(hangman_art.stages[6])
print(' '.join([str(elem) for elem in current_variant]))

# Main game condition check
while we_are_in_game:

    # The player guesses the letter 
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)) :
        if chosen_word[i] == guess:
            current_variant[i] = guess
    print(' '.join([str(elem) for elem in current_variant]))

    # The player lost the round
    if not (guess in chosen_word):
        lives_left -= 1
        print (hangman_art.stages[lives_left])

    # Check for victory / defeat
    if "_" not in current_variant:
        print(f"You win! {lives_left} lives left")
        we_are_in_game = False
    elif lives_left == 0:
        uncover = ' '.join([str(elem) for elem in chosen_word])
        print(f"You did not guess {uncover}!")
        we_are_in_game = False

