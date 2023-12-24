cantidad_numeros = int(input("Ingrese cuántos números va a ingresar: "))
mayor = float("-inf")
menor = float("inf")
suma = 0


for i in range(cantidad_numeros):
    numero = float(input("Ingrese número: "))
    
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    
    suma += numero

promedio = suma / cantidad_numeros

print("El mayor número que ingresó fue", mayor)
print("El menor número que ingresó fue", menor)
print("El promedio de los números es", promedio)