# Ataque de fuerza bruta al cifrado Cesar.
# Se prueban las 26 posibles claves y se busca
# el resultado que mas se parezca al castellano.

mensaje = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

abc = "abcdefghijklmnopqrstuvwxyz"

# Palabras frecuentes en castellano
palabras_es = [
    "el", "la", "los", "las",
    "de", "del", "en",
    "un", "una",
    "que", "y", "es",
    "por", "con", "para",
    "se", "al", "lo",
    "a", "como"
]


def descifrar(mensaje, clave):

    resultado = ""

    for char in mensaje:

        char = char.lower()

        # Si no es una letra, se mantiene igual
        if char not in abc:
            resultado += char
            continue

        # Desciframos desplazando hacia atras
        resultado += abc[(abc.index(char) - clave) % 26]

    return resultado


def puntuar(texto):

    palabras = texto.split()
    puntuacion = 0

    for palabra in palabras_es:

        # Quitamos la coma y otros signos
        palabra = palabra.strip(".,;:!?")

        if palabra in palabras:
            puntuacion += 1

    return puntuacion


def cesar(mensaje):

    mejor_clave = 0
    mejor_texto = ""
    mejor_puntuacion = -1

    # Probamos las 26 posibles claves
    for clave in range(26):

        resultado = descifrar(mensaje, clave)

        puntuacion = puntuar(resultado)

        print("Clave:", clave, "->", resultado)

        # Guardamos el resultado que mas
        # palabras en castellano tenga
        if puntuacion > mejor_puntuacion:

            mejor_puntuacion = puntuacion
            mejor_clave = clave
            mejor_texto = resultado

    return mejor_clave, mejor_texto


if __name__ == "__main__":

    print("Mensaje cifrado:", mensaje)

    clave, mensaje_descifrado = cesar(mensaje)

    print("\n--- Resultado ---")
    print("Clave encontrada:", clave)
    print("Mensaje descifrado:", mensaje_descifrado)