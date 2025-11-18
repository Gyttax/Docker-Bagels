import random  # Importa el módulo random para generar números aleatorios

DIGITS = 3  # Puedes cambiarlo después para números de más dígitos
MAX_GUESSES = 10  # Puedes cambiarlo después para más intentos


def main():

    print(
        f"""¡Bienvenido/a al juego Bagels! Un juego de deducción lógica. Estoy pensando en un número de {DIGITS} dígitos. ¡Intenta adivinarlo! Aquí tienes algunas pistas:
        
        Cuando digo:    Eso significa:
        
        Pico            Un dígito es correcto pero está en la posición equivocada.
        Fermi           Un dígito es correcto y está en la posición correcta.
        Bagels          Ningún dígito es correcto.

Por ejemplo, si el número secreto fuera 248 y tu conjetura fuera 843, la pista sería 'Fermi Pico'.

¡Vamos a jugar! ¡Buena suerte!"""
    )

    while True:  # Main loop del juego

        secretNum = (
            generate_secret_number()
        )  # Genera un número de N dígitos aleatorio sin repeticiones
        print("\nHe pensado un número. ¡Adivina cuál es!")
        print(f"Tienes {MAX_GUESSES} intentos para adivinarlo.")

        numGuesses = 1

        while numGuesses <= MAX_GUESSES:

            guess = ""
            while len(guess) != DIGITS or not guess.isdecimal():
                print(f"\nIntento #{numGuesses}: ")
                guess = input("> ")  # Recepción de la respuesta del usuario

                if (
                    len(guess) != DIGITS
                ):  # Validación de la longitud de dígitos recibida
                    print(f"\nIngresa exactamente {DIGITS} dígitos: ")

                elif not guess.isdecimal():  # Validación de que la entrada sea numérica
                    print(f"\nIngresa solo números: ")

            clues = get_clues(
                guess, secretNum
            )  # Obtención de pistas basadas en la conjetura
            print(clues)
            numGuesses += 1  # Incremento del número de intentos

            if guess == secretNum:  # Si el usuario acierta
                print("¡Felicidades! ¡Has adivinado el número!")
                break

            if numGuesses > MAX_GUESSES:  # Si el usuario no logra adivinar
                print("¡Se te han acabado los intentos!")
                print(f"El número era {secretNum}.")  # Se revela el número secreto

        respuesta = input(
            "¿Quieres jugar de nuevo? (s/n) \n>>> "
        )  # Pregunta para reiniciar el juego
        if not respuesta.lower().startswith(
            "s"
        ):  # Si la respuesta no es afirmativa, se termina el juego
            break

    print("¡Gracias por jugar!")


def generate_secret_number():
    """Este apartado estará generando el número secreto para adivinar
    La condición principal es que ningún dígito se repita por lo tanto:"""

    numbers = list("0123456789")
    random.shuffle(numbers)  # Mezcla los números aleatoriamente

    secretNum = ""
    for i in range(DIGITS):
        secretNum += str(
            numbers[i]
        )  # Selecciona los primeros 'digits' números de la lista mezclada
    return secretNum


def get_clues(guess, secretNum):

    if guess == secretNum:
        return "¡Has acertado!"

    clues = []

    for i in range(len(guess)):  # Recorre cada dígito en la conjetura

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
