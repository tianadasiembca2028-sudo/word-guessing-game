import random

words = {
    "Animals": ["tiger", "elephant", "penguin", "giraffe", "monkey"],
    "Technology": ["python", "computer", "internet", "keyboard", "software"],
    "Food": ["pizza", "burger", "noodles", "sandwich", "chocolate"],
    "Countries": ["india", "japan", "brazil", "canada", "france"]
}


def choose_category():
    print("\nChoose a category:")
    categories = list(words.keys())

    for i, category in enumerate(categories, 1):
        print(i, ".", category)

    while True:
        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]

        print("Please enter a valid choice.")


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy - 10 attempts")
    print("2. Medium - 8 attempts")
    print("3. Hard - 6 attempts")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 8
        elif choice == "3":
            return 6

        print("Please enter 1, 2, or 3.")


def play_game():
    print("\n==============================")
    print("      WORD GUESSING GAME")
    print("==============================")

    category = choose_category()
    attempts = choose_difficulty()

    word = random.choice(words[category])
    guessed_letters = []
    score = 0

    display_word = ["_"] * len(word)

    print("\nCategory:", category)
    print("The word has", len(word), "letters.")
    print("You have", attempts, "attempts.")

    while attempts > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Attempts left:", attempts)

        if guessed_letters:
            print("Guessed letters:", ", ".join(guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")

            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess

            score += 10

        else:
            print("Wrong guess!")
            attempts -= 1
            score -= 2

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word!")
        print("The word was:", word)
        print("Your score:", max(score, 0))
    else:
        print("\nGame Over!")
        print("The correct word was:", word)
        print("Your score:", max(score, 0))


def main():
    print("Welcome to the Word Guessing Game!")

    while True:
        play_game()

        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for playing!")
            break


main()
