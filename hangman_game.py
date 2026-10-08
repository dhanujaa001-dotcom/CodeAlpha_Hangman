import random

words = ["program", "computer", "keyboard", "function", "variable"]
secret = random.choice(words)

display = ["_"] * len(secret)
guessed = []
MAX_WRONG = 6
wrong = 0

print("===== HANGMAN =====")
print(f"Guess the word one letter at a time. You have {MAX_WRONG} incorrect guesses.")

while wrong < MAX_WRONG and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", ", ".join(guessed) if guessed else "-")
    print("Wrong guesses left:", MAX_WRONG - wrong)

    guess = input("Enter a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print(f"You already guessed '{guess}'. Try another.")
        continue

    guessed.append(guess)

    if guess in secret:
        print("Correct!")
        for i, letter in enumerate(secret):
            if letter == guess:
                display[i] = guess
    else:
        wrong += 1
        print(f"Wrong! '{guess}' is not in the word.")

print()
if "_" not in display:
    print(f'You won! The word was "{secret}".')
else:
    print(f'You lost! The word was "{secret}".')