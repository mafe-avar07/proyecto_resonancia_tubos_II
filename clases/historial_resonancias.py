class HistorialResonancias(object):

    def __init__(self):
        self.historial = []

    def agregar_resultado(self, frecuencia):
        self.historial.append(frecuencia)

    def mostrar_historial(self):

        if len(self.historial) == 0:
            print("No existen resultados registrados.")
            return

        print("\nHISTORIAL DE FRECUENCIAS")

        contador = 1

        for frecuencia in self.historial:

            print(str(contador) + ". " + str(round(frecuencia, 2)) + " Hz")

            contador += 1

    def calcular_promedio(self):

        if len(self.historial) == 0:
            return 0

        suma = 0

        for frecuencia in self.historial:
            suma += frecuencia

        promedio = suma / len(self.historial)

        return promedio

    def obtener_maximo(self):

        if len(self.historial) == 0:
            return 0

        mayor = self.historial[0]

        for frecuencia in self.historial:

            if frecuencia > mayor:
                mayor = frecuencia

        return mayor