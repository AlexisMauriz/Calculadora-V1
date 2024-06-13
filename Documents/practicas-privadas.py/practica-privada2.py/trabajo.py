class TarjetaSAETA:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def pagar_pasaje(self, costo_pasaje):
        if self.saldo >= costo_pasaje:
            self.saldo -= costo_pasaje
            return True
        else:
            return False


def main():
    saldo_inicial = 2000
    costo_pasaje = 110

    tarjeta = TarjetaSAETA(saldo_inicial)

    print("Ingrese 's' si su tarjeta es de SAETA.")
    print("Ingrese 'n' si su tarjeta no es de SAETA.")
    print("Ingrese 'i' si su tarjeta de SAETA no se lee.")

    while True:
        opcion = input("Ingresa tu opción: ").lower()

        if opcion == "s":
            if tarjeta.pagar_pasaje(costo_pasaje):
                print("Pase concedido.")
            else:
                print("Saldo insuficiente. Por favor recargue su tarjeta.")
            break
        elif opcion == "n":
            print("Tarjeta inválida. Intente nuevamente.")
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
