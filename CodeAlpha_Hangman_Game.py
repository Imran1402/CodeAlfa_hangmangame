import random

# List of predefined words
word_list = ["apple", "banana", "grape", "orange", "peach"]

# Choose a random word from the list
secret_word = random.choice(word_list)
guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(secret_word))

# Game loop
while tries > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        tries -= 1
        print(f"❌ Wrong! Tries left: {tries}")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check for win
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("💀 Game Over! The word was:", secret_word)
