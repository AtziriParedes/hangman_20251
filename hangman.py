# Base code hangman.py for project colaboration.

import random
import string

WORD_LIST = [
    "python", "desarrollo", "colaboracion", "github", "ahorcado",
    "programacion", "funcion", "variable", "algoritmo", "repositorio"
]

def choose_word():
    return random.choice(WORD_LIST).upper()

def display_state(word, guessed_letters):
    display = " ".join(c if c in guessed_letters else "_" for c in word)
    print(f"\nPalabra: {display}")
    print(f"Letras adivinadas: {', '.join(sorted(guessed_letters))}")

def get_guess(guessed_letters):
    while True:
        guess = input("Adivina una letra: ").strip().upper()
        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("→ Ingresa UNA sola letra A–Z.")
        elif guess in guessed_letters:
            print("→ Ya probaste esa letra.")
        else:
            return guess

def play():
    word = choose_word()
    guessed_letters = set()

    print("¡Bienvenido al juego del Ahorcado!")
    # Sigue hasta adivinar todas las letras
    while not all(c in guessed_letters for c in word):
        display_state(word, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        if guess in word:
            print(f"✔ ¡'{guess}' está en la palabra!")
        else:
            print(f"✖ '{guess}' no está en la palabra.")
    print(f"\n🎉 ¡Felicidades! Has adivinado la palabra: {word}")

if __name__ == "__main__":
    play()