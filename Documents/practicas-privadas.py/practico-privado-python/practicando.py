print("Ejercicio 40")
print()
print("Tabla de Multiplicar.")
print("Elegir una opción.")
print()
print("1 - Sumar")
print("2 - Restar")
print("3 - Multiplicar")
print("4 - Dividir")

opciones = {
    1: "Suma",
    2: "Resta",
    3: "Multiplicación",
    4: "División"
}

while True:
    usuario = input("Ingrese una opción: ")

    # Verificar si la entrada es numérica
    if not usuario.isdigit():
        print("Por favor, ingrese un número válido.")
        continue

    usuario = int(usuario)

    # Verificar si el usuario ha ingresado una opción válida
    if usuario not in opciones:
        print("Por favor, ingrese una opción válida (1, 2, 3, 4).")
        continue

    primer_numero = float(input("Ingrese el Primer número: "))
    segundo_numero = float(input("Ingrese el Segundo número: "))

    if usuario == 1:
        resultado = primer_numero + segundo_numero
    elif usuario == 2:
        resultado = primer_numero - segundo_numero
    elif usuario == 3:
        resultado = primer_numero * segundo_numero
    elif usuario == 4:
        if segundo_numero != 0:
            resultado = primer_numero / segundo_numero
        else:
            print("No se puede dividir entre cero.")
            continue  # Continuar con la siguiente iteración del bucle si se divide entre cero

    print(f"El resultado de la {opciones[usuario]} de {primer_numero} y {segundo_numero} es: {resultado}")

    # Preguntar al usuario si desea realizar otra operación
    continuar = input("¿Desea realizar otra operación? (S/N): ")
    if continuar.upper() != "S":
        break
