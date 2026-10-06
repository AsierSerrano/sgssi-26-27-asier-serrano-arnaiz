from collections import Counter


# ============================================================
# MENSAJE CIFRADO
# ============================================================

mensaje = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""


# Frecuencias aproximadas del castellano
FRECUENCIAS_ES = {
    "E": 16.78, "A": 11.96, "O": 8.69, "L": 8.37,
    "S": 7.88, "N": 7.01, "D": 6.87, "R": 4.94,
    "U": 4.80, "I": 4.15, "T": 3.31, "C": 2.92,
    "P": 2.78, "M": 2.12, "Y": 1.54, "Q": 1.53,
    "B": 0.92, "H": 0.89, "G": 0.73, "F": 0.52,
    "V": 0.39, "J": 0.30, "Ñ": 0.29, "Z": 0.15,
    "X": 0.06, "K": 0.00, "W": 0.00
}

ALFABETO = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")


# ============================================================
# FRECUENCIAS
# ============================================================

def mostrar_frecuencias():

    letras = [
        c.upper()
        for c in mensaje
        if c.isalpha()
    ]

    contador = Counter(letras)
    total = len(letras)

    print("\n--- FRECUENCIAS ---")

    for letra, cantidad in contador.most_common():

        porcentaje = cantidad / total * 100

        print(
            f"{letra}: {cantidad:3} "
            f"({porcentaje:5.2f}%)"
        )


# ============================================================
# DESCIFRAR
# ============================================================

def descifrar(texto, clave):

    resultado = ""

    for c in texto:

        if c.upper() in clave:

            letra = clave[c.upper()]

            if c.islower():
                resultado += letra.lower()
            else:
                resultado += letra

        else:
            resultado += "_"

    return resultado


# ============================================================
# PROPUESTA AUTOMÁTICA
# ============================================================

def propuesta_automatica():

    letras = [
        c.upper()
        for c in mensaje
        if c.isalpha()
    ]

    contador = Counter(letras)

    # Letras cifradas ordenadas por frecuencia
    cifradas = [
        letra
        for letra, cantidad in contador.most_common()
    ]

    # Letras españolas ordenadas por frecuencia
    castellano = sorted(
        FRECUENCIAS_ES,
        key=FRECUENCIAS_ES.get,
        reverse=True
    )

    clave = {}

    for cifrada, clara in zip(cifradas, castellano):
        clave[cifrada] = clara

    return clave


# ============================================================
# MOSTRAR CLAVE
# ============================================================

def mostrar_clave(clave):

    print("\n--- SUSTITUCIONES ---")

    if not clave:
        print("No hay sustituciones.")
        return

    for cifrada in sorted(clave):
        print(f"{cifrada} -> {clave[cifrada]}")


# ============================================================
# FUERZA BRUTA DE UNA LETRA
# ============================================================

def probar_letra(letra, clave):

    usadas = set(clave.values())

    print(f"\n--- PROBANDO {letra} ---")

    for candidata in ALFABETO:

        if candidata in usadas:
            continue

        prueba = clave.copy()
        prueba[letra] = candidata

        texto = descifrar(mensaje, prueba)

        print(f"\n{letra} -> {candidata}")
        print(texto[:300])


# ============================================================
# AYUDA
# ============================================================

def ayuda():

    print("""
COMANDOS:

  frecuencia
      Muestra las frecuencias del texto cifrado.

  auto
      Genera una propuesta automática usando
      las frecuencias del castellano.

  texto
      Muestra el texto con las sustituciones actuales.

  clave
      Muestra las sustituciones actuales.

  X=Y
      Cambia una sustitución.
      Ejemplo: R=C

  brute X
      Prueba distintas letras para X.

  borrar X
      Elimina una sustitución.

  reset
      Borra todas las sustituciones.

  ayuda
      Muestra esta ayuda.

  salir
      Termina el programa.
""")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

print("=== ATAQUE DE FUERZA BRUTA POR SUSTITUCIÓN ===")

print("""
La propuesta automática usa el análisis de frecuencias.
Puedes modificarla manualmente en cualquier momento.
""")

clave = {}

ayuda()

while True:

    comando = input("\n> ").strip()

    if not comando:
        continue

    # --------------------------------------------------------
    # SALIR
    # --------------------------------------------------------

    if comando.lower() == "salir":
        break

    # --------------------------------------------------------
    # AYUDA
    # --------------------------------------------------------

    elif comando.lower() == "ayuda":
        ayuda()

    # --------------------------------------------------------
    # FRECUENCIAS
    # --------------------------------------------------------

    elif comando.lower() == "frecuencia":
        mostrar_frecuencias()

    # --------------------------------------------------------
    # PROPUESTA AUTOMÁTICA
    # --------------------------------------------------------

    elif comando.lower() == "auto":

        clave = propuesta_automatica()

        print("\n--- PROPUESTA AUTOMÁTICA ---")
        mostrar_clave(clave)

        print("\n--- TEXTO PROPUESTO ---")
        print(descifrar(mensaje, clave))

    # --------------------------------------------------------
    # MOSTRAR TEXTO
    # --------------------------------------------------------

    elif comando.lower() == "texto":

        print("\n--- TEXTO ACTUAL ---")
        print(descifrar(mensaje, clave))

    # --------------------------------------------------------
    # MOSTRAR CLAVE
    # --------------------------------------------------------

    elif comando.lower() == "clave":

        mostrar_clave(clave)

    # --------------------------------------------------------
    # REINICIAR
    # --------------------------------------------------------

    elif comando.lower() == "reset":

        clave = {}

        print("Todas las sustituciones han sido borradas.")

    # --------------------------------------------------------
    # BORRAR UNA LETRA
    # --------------------------------------------------------

    elif comando.lower().startswith("borrar "):

        partes = comando.split()

        if len(partes) == 2 and len(partes[1]) == 1:

            letra = partes[1].upper()

            if letra in clave:

                del clave[letra]

                print(f"Se ha borrado {letra}.")
                print(descifrar(mensaje, clave))

            else:

                print("Esa letra no tiene sustitución.")

        else:

            print("Uso: borrar X")

    # --------------------------------------------------------
    # FUERZA BRUTA DE UNA LETRA
    # --------------------------------------------------------

    elif comando.lower().startswith("brute "):

        partes = comando.split()

        if len(partes) == 2 and len(partes[1]) == 1:

            letra = partes[1].upper()

            if letra in ALFABETO:

                probar_letra(letra, clave)

            else:

                print("Letra no válida.")

        else:

            print("Uso: brute X")

    # --------------------------------------------------------
    # CAMBIAR UNA SUSTITUCIÓN
    # --------------------------------------------------------

    elif "=" in comando:

        partes = comando.split("=")

        if len(partes) == 2:

            cifrada = partes[0].strip().upper()
            clara = partes[1].strip().upper()

            if len(cifrada) != 1 or len(clara) != 1:

                print("Usa el formato X=Y")

                continue

            if cifrada not in ALFABETO or clara not in ALFABETO:

                print("Letra no válida.")

                continue

            # Si otra letra ya utiliza esa letra clara,
            # eliminamos esa asignación.
            for letra in list(clave):

                if letra != cifrada and clave[letra] == clara:

                    del clave[letra]

            clave[cifrada] = clara

            print(f"\nCambio realizado: {cifrada} -> {clara}")

            print("\n--- TEXTO ACTUAL ---")
            print(descifrar(mensaje, clave))

        else:

            print("Usa el formato X=Y")

    # --------------------------------------------------------
    # COMANDO DESCONOCIDO
    # --------------------------------------------------------

    else:

        print("Comando no reconocido.")
        print("Escribe 'ayuda' para ver los comandos.")


print("\n=== RESULTADO FINAL ===")
print(descifrar(mensaje, clave))
