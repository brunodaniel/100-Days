import random
import hangman_art
import hangman_words
import os


lives = 6


result = []
chosen_word = random.choice(hangman_words.word_list)
word_lenght = len(chosen_word)
end_of_game = False

for i in range(word_lenght):
    result.append("_")

print(hangman_art.logo)
while not end_of_game:

    guess = input("Choose a letter: ")
    os.system('cls||clear')
    for i in range(word_lenght):
        if chosen_word[i] == guess:
            result[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You loose a live")
        if lives == 0:
            print("You Loose")
            end_of_game = True
    else:
        print(f"The letter {guess} was already chosen")
    print(f"{' '.join(result)}")

    if "_" not in result:
        end_of_game = True
        print("You Win")
    print(hangman_art.stages[lives])
