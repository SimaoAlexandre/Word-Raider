import random


game_title = "Word Raider"

word_bank = []

with open("words.txt") as word_file:
    for w in word_file:
        word_bank.append(w.rstrip().lower())

word_to_guess = random.choice(word_bank)
max_turns = 5
turns_taken = 0

misplaced_letters = []
incorrect_letters = []

print(f"Welcome to {game_title}!")
print(f"You have {max_turns} attempts to guess the word.")

while turns_taken < max_turns:
    
    guess = input("Guess a word: ").lower()

    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please enter 5-letter word.")
    else:
        index = 0
        for c in guess:
            if c == word_to_guess[index]:
                print(c, end=" ")
                if c in misplaced_letters:
                    misplaced_letters.remove(c)
            elif c in word_to_guess:
                if c not in misplaced_letters:
                    misplaced_letters.append(c)
                print("_", end=" ")
            else:
                if c not in incorrect_letters:
                    incorrect_letters.append(c)
                print("_", end=" ")
            index += 1

        print("\n")
        print("Misplaced letters: ", misplaced_letters)
        print("Incorrect letters: ", incorrect_letters)
        turns_taken += 1

    if guess == word_to_guess:
        print("Congratulations, you win!")
        break

    if turns_taken == max_turns:
        print("Sorry, you lost. The word was", word_to_guess)
        break



if (turns_taken == max_turns): print(f"Sorry, you've used all your attempts. The word was '{word_to_guess}'.")