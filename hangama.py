import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "coding", "logic", "script", "laptop"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("--- Welcome to Hangman! ---")
    
    while attempts > 0:
        # Display current progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        
        # Check if player won
        if "_" not in display_word:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'.")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not there.")

    if attempts == 0:
        print(f"\nGame Over! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()
