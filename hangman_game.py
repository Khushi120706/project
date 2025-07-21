import random

WORDS = ['python', 'hangman', 'challenge', 'programming', 'computer']
MAX_TRIES = 6

def choose_word():
    return random.choice(WORDS)

def display_word(word, guessed):
    return ' '.join([c if c in guessed else '_' for c in word])

def hangman():
    word = choose_word()
    guessed = set()
    tries = MAX_TRIES

    print("Welcome to Hangman!")
    while tries > 0:
        print(f"\nWord: {display_word(word, guessed)}")
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)
        if guess in word:
            print("Good guess!")
            if all(c in guessed for c in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            print("Wrong guess!")
            tries -= 1
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()