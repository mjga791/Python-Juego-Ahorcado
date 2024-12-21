import random

# Creamos una función que seleccione una palabra al azar de una lista dada
# -> str: indica que la lista palabras contendrá sólo stings
def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript','java', 'angular', 'django', 'tensorflow', 'react', 'typescript', 'git', 'flask']
    return random.choice(palabras)

# Para mostrar las letras que se van adivinando
def mostrar_progreso(palabra_secreta, letras_adivinadas):
    # Indicalmente la variable adivinado estará vacía
    adivinado = ''
    # Hacemos un bucle en el que si la letra es correcta, la muestra 
    # y si no pone _ en su lugar    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    # El juego comienza llamando a la función que genera la palabra al azar
    palabra_secreta = obtener_palabra_secreta()
    # Se crea una lista vacía con las letras que vaya adivinando el jugador
    letras_adivinadas = []
    # Se establece que el número de intentos sea la longitud de la palabra sercreta
    intentos = len(palabra_secreta)
    juego_terminado = False

    print("¡Vamos a jugar al Juego del Ahorcado!")
    print(f"Dispones de {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "La cantidad de letras de la palabra es:", len(palabra_secreta))

    # El juego seguirá hasa que aparezca juego terminado o bien se acaben los intentos
    while not juego_terminado and intentos > 0:
        # Puesto que en el listado del que saca una palabra al azar
        # están todas escritas en minúsculas, con .lower nos aseguramosç
        # de pasar lo que escriba el usuario a minúsculas
        letra_introducida = input("Di una letra: ").lower()
        # Para asegurarse de que la entrada sólo de una letra
        if len(letra_introducida) != 1 or not letra_introducida.isalpha():
            print("Por favor, recuerda que sólo puedes decir una letra cada vez")
        # Para asegurarnos de que la letra introducida por jugador no se repita
        elif letra_introducida in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        # En caso de que se haya introducido una letra y no esté repetida
        # se añade al array de letras adivinadas
        else:
            letras_adivinadas.append(letra_introducida)

            if letra_introducida in palabra_secreta:
                print(f"¡Estupendo, la letra '{letra_introducida}' está presente en la palabra")
            else:
                # Para disminuir el número de intentos, en caso de que la letra no se adivine
                intentos -= 1
                print(f"Vaya, lo siento, la letra '{letra_introducida}' no está presente en la palabra secreta")
                print(f"Te quedan {intentos} intentos")

        # Para que imprima la letra que se ha adivinado o siga mostrando "_"
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        # Sabremos que el juego ha terminado cuando ya no quede ningun "_"
        if "_" not in progreso_actual:
            juego_terminado = True
            # Muestra la palabra con la primera letra en mayúscula
            palabra_secreta = palabra_secreta.capitalize()
            print(f"¡Enhorabuena, conseguiste completar la palabra: '{palabra_secreta}'")

    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"¡Qué pena! Se te han acabado los intentos\n La palabra secreta era '{palabra_secreta}'")

    jugar_de_nuevo = input("¿Quieres jugar otra vez? (sí/no): ").strip().lower()
    if jugar_de_nuevo == 'sí' or 'si' or 's':
        juego_ahorcado()
    else:
        if jugar_de_nuevo == 'no':
            print("Cuando te apetezca, volvemos a jugar")
        else:
            print(f"Como has dicho {jugar_de_nuevo}, entiendo que quieres decir no. Así que, hasta la próxima")

juego_ahorcado()