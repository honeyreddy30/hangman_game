import random
from movies_list import movies_list

chosen_word = random.choice(movies_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from ascii_art import logo
print(logo)


display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess the letter: ").lower()
    if guess in display:
        print("You've already guessed this letter")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives <= 0:
            print("You Lose😞. Better luck next time")
            end_of_game = True    
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win, Wohoooooo🥳")
    from ascii_art import stages
    print(stages[lives])
print(f"REVELATION: The chosen word was {chosen_word}")
        
