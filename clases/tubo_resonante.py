class TuboResonante(object):

    def __init__(self, longitud, velocidad_sonido):
        self.longitud = longitud
        self.velocidad_sonido = velocidad_sonido
        self.frecuencia_fundamental = 0

    def calcular_fundamental(self):
        self.frecuencia_fundamental = (self.velocidad_sonido/(4 * self.longitud))
        return self.frecuencia_fundamental

    def calcular_armonico(self, numero_armonico):
        frecuencia = (numero_armonico * self.velocidad_sonido/(4 * self.longitud))
        return frecuencia

    def mostrar_resultados(self):
        print(f"Longitud: {self.longitud} m")
        print(f"Velocidad del sonido: {self.velocidad_sonido} m/s")
        print(f"Frecuencia fundamental: "f"{self.frecuencia_fundamental:.2f} Hz")