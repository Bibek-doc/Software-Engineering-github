import random

def image():
    words_list = ["start", "random", "generate", "user"]
    word = random.choice(words_list)
    blanks = ["_"] * len(word)  # Generate blanks for each letter
    lives = 7

    while True:
        print(" ".join(blanks))
        guess = input("Guess a letter: ").lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    blanks[i] = guess
            if "_" not in blanks:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            lives -= 1
            print(f"Wrong guess! Lives left: {lives}")
            if lives == 0:
                print("Game Over! The word was:", word)
                break