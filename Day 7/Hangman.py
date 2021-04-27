import random
import art
import random_word

print(art.logo)

chosen_word = random.choice(random_word.word_list)
# Testing code
print(f'Psst, the solution is {chosen_word}.')

# TODO: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
#  guess.

display = ('_ ' * len(chosen_word)).split()
# TODO: - Create a variable called 'lives' to keep track of the number of lives left.
#   Set 'lives' to equal 6.
lives = 6
# TODO: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#  letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
letterAlready = []
while True:
    guess: str = input("Guess a letter: ").lower()
    # TODO: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in letterAlready:
        print('You already entre This Character')
    # TODO: - Loop through each position in the chosen_word;
    #   If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #   e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    if not (guess in letterAlready):
        letterAlready.append(guess)
        if guess in chosen_word:
            for i in range(0, len(chosen_word)):
                if guess == chosen_word[i]:
                    display[i] = guess
            print(display)
        else:
            print('You Enter Character isn\'t in word, you lose a life !')
            print('--------------------------------')
            print(art.stages[lives])
            if lives == 0:
                print('You Are Loser !')
                break
            lives -= 1

        # TODO: - If guess is not a letter in the chosen_word,
        #   Then reduce 'lives' by 1.
        #   If lives goes down to 0 then the game should stop and it should print "You lose."
        if not ('_' in display):
            print('You are winner !️')
            break

