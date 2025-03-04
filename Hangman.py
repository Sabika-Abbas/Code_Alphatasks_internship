import random
import string

words = {"Oxygen" :"Essential for breathing",
"Giraffe" : "Tallest land animal",
"Pyramid": "Ancient Egyptian structure",
"Galaxy" : "Collection of stars and planets",
"Whistle" : "High-pitched sound or object",
"Jigsaw" : "Type of puzzle",
"Thunder" : "Loud sound after lightning",
"Lantern" : "Portable light source",
"Castle" : "Fortress for royalty",
"Volcano" : "Erupts with lava",
"Compass" : "Used for navigation",
"Fossil" : "Preserved remains of ancient life",
"Icicle" : "Frozen water hanging down",
"Parrot" : "Colorful talking bird",
"Helmet" : "Protective headgear",
"Banana" : "Yellow curved fruit",
"Glacier" : "Large ice formation",
"Cactus" : "Spiky desert plant",
"Jungle" : "Dense tropical forest",
"Rocket" : "Space-travel vehicle"}

def get_valid_word():
    # Select a random word and its hint
    word = random.choice(list(words.keys())).lower()
    hint = words[word.capitalize()]
    return word,hint

def hangman():
    word, hint = get_valid_word()
    word_letter = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letter = set()
    lives = 8

    while len(word_letter) > 0 and lives > 0:
        print("Lives:", lives, ", Used letters:", ' '.join(used_letter))
        print(f"Hint:{hint}")
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print("Current word:", ' '.join(word_list))
        guess = input("Guess a letter: ").lower()

        if guess in alphabet - used_letter:
            used_letter.add(guess)
            if guess in word_letter:
                word_letter.remove(guess)
            else:
                lives -= 1
                print(guess, "not present in the word")

        elif guess in used_letter:
            print("You have already guessed this letter")

        else:
            print('Invalid')

    if len(word_letter) == 0:
        print("You win! The word is:", word)
    else:
        print("You lose! The word was", word)

print("Welcome to Hangman")
hangman()
while True:
    cont=input("Continue playing? y for yes n for No: ").lower()
    if cont=="y":
        hangman()
    elif cont=="n":
        break
    else:
        print("Invalid Choice")

