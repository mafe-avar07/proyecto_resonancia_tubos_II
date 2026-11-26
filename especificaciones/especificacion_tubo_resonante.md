Nombre de la clase:
TuboResonante

Objetivo:
Representar una columna de aire cerrada capaz de calcular frecuencias resonantes y armónicos.

Responsabilidad:
Almacenar los datos físicos del problema y realizar los cálculos relacionados con la resonancia.


Atributos:
longitud
Tipo: float
Unidad: metros
Significado: longitud de la columna de aire.

velocidad_sonido
Tipo: float
Unidad: m/s
Significado: velocidad de propagación del sonido.

frecuencia_fundamental
Tipo: float
Valor inicial: 0.0
Significado: frecuencia correspondiente al primer armónico.

Constructor
__init__(longitud, velocidad_sonido)
Inicializa los atributos de la clase con los valores proporcionados por el usuario.


Métodos:
calcular_fundamental()

Calcula la frecuencia fundamental usando:
f = v / (4L)
Retorna la frecuencia fundamental.

Calcular_armonico(numero_armonico):
Calcula la frecuencia del armónico solicitado.
Solo se permiten armónicos impares.
Retorna la frecuencia calculada.

mostrar_resultados()
Muestra todos los resultados obtenidos.


Validaciones:
longitud > 0
velocidad_sonido > 0
armónico impar positivo


Reglas para el agente:
Usar la fórmula de columna cerrada.
Permitir solo armónicos impares.
No agregar métodos adicionales.
No utilizar bibliotecas externas.
No modificar las fórmulas físicas.