from clases.tubo_resonante import TuboResonante
from clases.historial_resonancias import HistorialResonancias


def mostrar_menu():
    print(" ANALIZADOR DE RESONANCIA:")
    print("1. Calcular frecuencia fundamental")
    print("2. Calcular armónico")
    print("3. Mostrar historial")
    print("4. Mostrar promedio")
    print("5. Mostrar frecuencia máxima")
    print("0. Salir")


def main():

    historial = HistorialResonancias()

    opcion = ""

    while opcion != "0":

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            longitud = float(input("Ingrese la longitud (m): "))

            velocidad = float(input("Ingrese la velocidad del sonido (m/s): "))

            tubo = TuboResonante(longitud, velocidad)

            frecuencia = (tubo.calcular_fundamental())

            historial.agregar_resultado(frecuencia)

            print("\nFrecuencia fundamental:")

            print(round(frecuencia, 2),"Hz")

        elif opcion == "2":

            longitud = float(input("Ingrese la longitud (m): "))

            velocidad = float(input("Ingrese la velocidad del sonido (m/s): "))

            armonico = int(input("Ingrese el armónico impar: "))

            if armonico % 2 == 0:

                print("Solo se permiten armónicos impares.")

            else:

                tubo = TuboResonante(longitud,velocidad)

                frecuencia = (tubo.calcular_armonico(armonico))

                historial.agregar_resultado(frecuencia)

                print("\nFrecuencia del armónico:")

                print(round(frecuencia, 2),"Hz")

        elif opcion == "3":

            historial.mostrar_historial()

        elif opcion == "4":

            promedio = (historial.calcular_promedio())

            print("\nPromedio:")

            print(round(promedio, 2),"Hz")

        elif opcion == "5":

            mayor = (historial.obtener_maximo())

            print("\nFrecuencia máxima:")

            print(round(mayor, 2),"Hz")

        elif opcion != "0":

            print("Opción no válida.")

    print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()