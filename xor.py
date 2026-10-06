# Cifrado de flujo mediante XOR

mensaje = "ATAQUE AL AMANECER"
clave = "CLAVE1234567890123"


def xor(mensaje, clave):
    resultado = []

    for i in range(len(mensaje)):
        resultado.append(mensaje[i] ^ clave[i])

    return bytes(resultado)


# Convertimos el mensaje y la clave a bytes
mensaje = mensaje.encode()
clave = clave.encode()

# Comprobamos que tengan la misma longitud
if len(mensaje) != len(clave):

    print("Error: el mensaje y la clave deben tener la misma longitud.")
    print("Longitud del mensaje:", len(mensaje), "bytes")
    print("Longitud de la clave:", len(clave), "bytes")

else:

    # Cifrado
    criptograma = xor(mensaje, clave)

    # Descifrado: XOR con la misma clave
    mensaje_descifrado = xor(criptograma, clave)

    print("Mensaje original:     ", mensaje)
    print("Mensaje en hexadecimal:", mensaje.hex().upper())

    print("Clave:                ", clave)
    print("Clave en hexadecimal: ", clave.hex().upper())

    print("Criptograma:          ", criptograma.hex().upper())

    print("Mensaje descifrado:   ", mensaje_descifrado.decode())

    # Comprobación
    print("¿Descifrado correcto?:", mensaje_descifrado == mensaje)
