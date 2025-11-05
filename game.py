import random

digits = 3  # cambialo después
max_guesses = 10  # cambialo después


def main():

    print(
        f"""¡Bienvenido/a al juego Bagels! Un juego de deducción lógica. Estoy pensando en un número de {digits} dígitos. ¡Intenta adivinarlo! Aquí tienes algunas pistas:
        
        Cuando digo:    Eso significa:
        
        Pico            Un dígito es correcto pero está en la posición equivocada.
        Fermi           Un dígito es correcto y está en la posición correcta.
        Bagels          Ningún dígito es correcto.

Por ejemplo, si el número secreto fuera 248 y tu conjetura fuera 843, la pista sería 'Fermi Pico'.""".format(
            digits
        )
    )

    while True:  # Main loop del juego

        secretNum = generate_secret_number()
        print("\nHe pensado un número. ¡Adivina cuál es!")
        print(f"(Tienes {max_guesses} intentos para adivinarlo.)".format(max_guesses))

        print(secretNum)  # Línea para pruebas, eliminar en producción

        numGuesses = 1

        while numGuesses <= max_guesses:

            guess = ""
            while len(guess) != digits or not guess.isdecimal():
                print(f"\nIntento #{numGuesses}: ")
                guess = print(input("> "))

            clues = get_clues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print("¡Felicidades! ¡Has adivinado el número!")
                break

            if numGuesses > max_guesses:
                print("¡Se te han acabado los intentos!")
                print(f"El número era {secretNum}.")

        respuesta = input("¿Quieres jugar de nuevo? (s/n) \n>>> ")
        if not respuesta.lower().startswith("s"):
            break

    print("¡Gracias por jugar!")


def generate_secret_number():

    # Este apartado estará generando el número secreto para adivinar
    # La condición principal es que ningún dígito se repita por lo tanto:

    numbers = list("0123456789")
    random.shuffle(numbers)  # Mezcla los números aleatoriamente

    secretNum = ""
    for i in range(digits):
        secretNum += str(
            numbers[i]
        )  # Selecciona los primeros 'digits' números de la lista mezclada
    return secretNum


def get_clues(guess, secretNum):

    if guess == secretNum:
        return "¡Has acertado!"

    clues = []

    for i in range(len(guess)):

        if guess[i] == secretNum[i]:
            clues.append("Fermi")  # Dígito correcto en la posición correcta

        elif guess[i] in secretNum:
            clues.append("Pico")  # Dígito correcto en la posición incorrecta

    if len(clues) == 0:
        return "Bagels"  # Ningún dígito es correcto

    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
