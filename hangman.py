#https://github.com/NetanelPardes/hangman

import random

WORDS = [
    "apple", "banana", "orange", "grape", "melon",
    "water", "house", "table", "chair", "window",
    "school", "teacher", "student", "pencil", "paper",
    "computer", "keyboard", "mouse", "screen", "phone",
    "music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest",
    "animal", "tiger", "lion", "zebra", "monkey",
    "rabbit", "horse", "sheep", "goat", "camel",
    "bird", "eagle", "snake", "fish", "shark",
    "pizza", "bread", "cheese", "salad", "soup",
    "coffee", "sugar", "honey", "butter", "cookie",
    "happy", "angry", "funny", "quiet", "brave",
    "smart", "strong", "clean", "dirty", "small",
    "large", "short", "long", "early", "late",
    "green", "yellow", "purple", "black", "white",
    "silver", "gold", "brown", "pink", "blue",
    "summer", "winter", "spring", "autumn", "season",
    "morning", "night", "today", "tomorrow", "yesterday",
    "family", "father", "mother", "brother", "sister",
    "friend", "people", "child", "baby", "woman",
    "man", "doctor", "driver", "soldier", "police",
    "engineer", "artist", "farmer", "chef", "pilot",
    "city", "village", "street", "bridge", "garden",
    "market", "store", "hotel", "airport", "station",
    "travel", "ticket", "train", "plane", "bottle",
    "camera", "picture", "letter", "number", "answer",
    "question", "game", "winner", "player", "score",
    "level", "start", "finish", "secret", "danger",
    "dream", "story", "movie", "book", "lesson",
    "language", "english", "hebrew", "word", "sentence",
    "voice", "sound", "light", "shadow", "fire",
    "earth", "stone", "metal", "wood", "glass",
    "cloud", "rain", "storm", "snow", "wind",
    "heart", "brain", "hand", "finger", "shoulder",
    "body", "face", "mouth", "tooth", "eye",
    "jump", "run", "walk", "swim", "drive",
    "write", "read", "speak", "listen", "learn",
    "build", "break", "open", "close", "catch",
    "throw", "bring", "carry", "choose", "change",
    "create", "delete", "search", "print", "input",
    "output", "random", "python", "function", "variable",
    "loop", "condition", "string", "list", "index",
    "error", "program", "project", "folder", "file"
]
MAX_TRY = 10

#get a random word from a list
def choose_random_word(word_list):
    return random.choice(word_list)

#Creating a hidden word
def hiding_word(secret_word):
    return "_" * len(secret_word)

#Prints the player's state in the game.
def printing_mode(hiding_word, guessing_balance,used_characters):
    print(f"Your successful guesses: {hiding_word} \nYou have {guessing_balance} guesses left.\
          \nThe characters you used: {used_characters}")

#Checks that the player typed a single letter and not something else
def letter_check(letter):
    return (letter.isalpha() and len(letter) == 1)

#Checks if the signal already exists
def letter_already_exists(letter, letter_list):
    return letter in letter_list

#Adding a letter to the guess list
def adding_letter_to_list(user_letter , letter_list):
    letter_list.append(user_letter)
    letter_list.sort()
    return letter_list

#Checks if the letter in the word is mysterious
def successful_letter_guess(letter,secret_word):
    return letter in secret_word

#Replace the hidden word with the correct letter.
def change_hidden_word(letter, my_hidden_word ,secret_word):
    my_hidden_word = list(my_hidden_word)
    for index, char in enumerate(secret_word):
        if char == letter:
            my_hidden_word[index] = letter
    return "".join(my_hidden_word)

#Checks if the user has used all of their attempts
def number_guesses_over(guessing_balance,secret_word):
    if guessing_balance == 0:
        print(f"🫷 game over \nteh secret word was {secret_word}")
    else:
        print("❌ Wrong guess\n")

#Checks if the user was able to guess the word
def successful_word_guessing(hidden_word ,secret_word):
    if hidden_word == secret_word:
        print(f"🏆 you win, good job! \nthe word are: {secret_word}\n")
    else:
        print("✅ Good job, keep it up\n.")

#The game itself
def start_game():
    my_secret_word = choose_random_word(WORDS)
    my_hiding_word = hiding_word(my_secret_word)
    guessing_balance = MAX_TRY
    used_characters = []
    
    while my_hiding_word != my_secret_word and guessing_balance > 0:
        printing_mode(my_hiding_word,guessing_balance,used_characters)
        user_letter = input("What letter do you want to guess? ").lower()

        if not letter_check(user_letter):
            print("❌ Error, typing an incorrect character\n")
            continue

        elif letter_already_exists(user_letter,used_characters):
            print("❌ You have already typed this letter\n")
            continue
        
        used_characters = adding_letter_to_list(user_letter,used_characters)

        if not successful_letter_guess(user_letter , my_secret_word):
            guessing_balance -= 1
            number_guesses_over(guessing_balance,my_secret_word) 
        else:
            my_hiding_word = change_hidden_word(user_letter , my_hiding_word , my_secret_word)
            successful_word_guessing(my_hiding_word , my_secret_word)

def main():
    start_game()


if __name__ == "__main__":
    main()