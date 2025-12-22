import random


def generar_secreto(limite: int) -> int:
    """Genera el número secreto entre 1 y limite (incluyente)."""
    return random.randint(1, limite)


def leer_entero(mensaje: str) -> int:
    """Lee un entero desde consola; repite hasta que el usuario ingrese un valor válido."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")


def obtener_pista(secreto: int, intento: int, pistas: dict[str, str]) -> str:
    """Devuelve el mensaje de pista según comparación."""
    if intento < secreto:
        return pistas["mayor"]
    if intento > secreto:
        return pistas["menor"]
    return ""


def jugar_adivina(limite: int = 10) -> None:
    secreto = generar_secreto(limite)

    # Estructura de datos (cinco palabras maximo)
    pistas = {
        "mayor": "No, mi número es mayor.",
        "menor": "No, mi número es menor.",
    }

    intentos = 0          # contador
    suma_intentos = 0     # acumulador (para demostrar uso; aquí suma 1 por intento)

    while True:
        intento = leer_entero(f"¿Qué número estoy pensando? (1-{limite}): ")

        # condicional: validación de rango
        if not (1 <= intento <= limite):
            print(f"Fuera de rango. Debe ser 1 a {limite}.")
            continue

        intentos += 1
        suma_intentos += 1

        if intento == secreto:
            break

        print(obtener_pista(secreto, intento, pistas), "Inténtalo de nuevo.")

    print(f"✅ ¡Correcto! Mi número era {secreto}. Intentos: {intentos}.")
    print(f"(Acumulador) Suma de intentos: {suma_intentos}")


if __name__ == "__main__":
    jugar_adivina(10)
