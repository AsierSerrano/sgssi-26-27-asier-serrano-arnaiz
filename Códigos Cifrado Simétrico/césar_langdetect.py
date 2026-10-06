# Ataque de fuerza bruta al cifrado Cesar.
# Se prueban las 26 posibles claves y se utiliza
# la deteccion de idioma para encontrar el mensaje
# en castellano.

from langdetect import detect


mensaje = "Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"

abc = "abcdefghijklmnopqrstuvwxyz"


def cesar(mensaje):

    # Probamos todas las posibles claves
    for clave in range(26):

        resultado = ""

        # Recorremos todos los caracteres del mensaje
        for char in mensaje:

            char = char.lower()

            # Si no es una letra, la dejamos igual
            if char not in abc:
                resultado += char
                continue

            # Desplazamos la letra
            resultado += abc[(abc.index(char) + clave) % 26]

        # Comprobamos si el resultado esta en castellano
        try:
            if detect(resultado) == "es":
                return clave, resultado

        except:
            pass

    return None


if __name__ == "__main__":

    clave, mensaje_descifrado = cesar(mensaje)

    print("Mensaje cifrado:", mensaje)
    print("Clave encontrada:", clave)
    print("Mensaje descifrado:", mensaje_descifrado)
