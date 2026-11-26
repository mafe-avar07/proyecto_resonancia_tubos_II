Nombre de la clase:
HistorialResonancias

Objetivo:
Almacenar y administrar los resultados obtenidos durante la ejecución del programa.

Responsabilidad:
Guardar los análisis realizados y proporcionar información estadística básica.


Atributos:
historial
Tipo: list
Valor inicial: []
Significado: almacena las frecuencias calculadas.

Constructor
__init__()
Inicializa una lista vacía.

Métodos
agregar_resultado(resultado)
Agrega un nuevo resultado al historial.

mostrar_historial()
Muestra todos los resultados almacenados.

calcular_promedio()
Calcula el promedio de las frecuencias registradas.

obtener_maximo()
Obtiene la frecuencia más alta almacenada.


Validaciones:
No calcular estadísticas si la lista está vacía.


Reglas para el agente:
Utilizar una lista para almacenar resultados.
No agregar estructuras de datos distintas.
No utilizar bibliotecas externas.
Mantener una responsabilidad exclusiva de almacenamiento y consulta.