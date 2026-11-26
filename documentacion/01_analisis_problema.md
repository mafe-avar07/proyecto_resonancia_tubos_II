1.  Nombre del problema y asignatura donde se estudió. 
    Análisis de resonancia en una columna de aire cerrada.
    Física I.

2.  Descripción, justificación y planteamiento original. 
    La resonancia es un fenómeno físico que ocurre cuando un sistema vubra con mayor 
    amplitud al ser excitado a una frecuencia específica denominada frecuencia de resonancia. 
    En las columnas de aire cerradas, únicamente pueden formarse armónicos impares debido 
    a las condiciones de frontera presentes en el sistema.
    
    El problema original consiste en determinar la frecuencia producida por un oscilador utilizando 
    la longitud de una columna de aire que entra en resonancia. Posteriormente se 
    determinan las siguientes longitudes que permiten obtener resonancias sucesivas.

    
    Este problema fue estudiado previamente en la asignatura de Física I y requiere la aplicación de 
    conceptos relacionados con ondas mecánicas, velocidad del sonido, frecuencia, longitud de onda y armónicos.
    
    Se seleccionó este problema porque involucra cálculos físicos, reglas matemáticas claramente definidas 
    y puede ampliarse mediante programación orientada a objetos para analizar múltiples situaciones de resonancia.

3.  Entradas: nombre, tipo de dato, restricciones y significado. 
    Longitud de la columna de aire:
        Tipo: float
        Unidad: metros (m)
        Restricción: valor mayor que cero.
        Significado: longitud de la columna de aire que produce resonancia.

    Velocidad del sonido:
        Tipo: float
        Unidad: metros por segundo (m/s)
        Restricción: valor mayor que cero.
        Significado: velocidad de propagación del sonido en el medio.

    Número de armónico:
        Tipo: int
        Restricción: números impares positivos (1, 3, 5, 7, ...)
        Significado: armónico que se desea analizar.

4.  Procesos: operaciones, fórmulas, reglas y decisiones. 
    Cálculo de la frecuencia fundamental:
        Para una columna de aire cerrada:
            f₁ = v / (4L)
                f₁ = frecuencia fundamental
                v = velocidad del sonido
                L = longitud de la columna de aire

    Cálculo de armónicos impares:
        fₙ = n(v / 4L)
            n = número impar del armónico

    Obtención de longitudes resonantes:
        Lₙ = n(v / 4f)
        para valores impares de n.

    Validaciones
        La longitud debe ser mayor que cero.
        La velocidad del sonido debe ser mayor que cero.
        El armónico seleccionado debe ser impar.
        No se permitirán valores negativos.

    Almacenamiento de resultados:
        Los resultados de cada análisis se almacenarán en una lista para generar un historial de consultas realizadas durante la ejecución del programa.

5.  Salidas esperadas. 
    La aplicación deberá mostrar:
        Frecuencia fundamental.
        Frecuencia de los armónicos solicitados.
        Longitudes resonantes correspondientes.
        Historial de análisis realizados.
        Estadísticas básicas de los resultados almacenados.

6.  Ejemplo original resuelto: datos, procedimiento y resultado. 
    Datos:
        Longitud de la columna de aire = 0.09 m
        Velocidad del sonido = 343 m/s

    Procedimiento:
        Aplicando la ecuación para la frecuencia fundamental:
        f₁ = v / (4L)
        f₁ = 343 / (4 × 0.09)
        f₁ = 952.77 Hz
        Posteriormente se pueden calcular las siguientes resonancias utilizando los armónicos impares.

    Resultado:
    Frecuencia fundamental: 952.77 Hz
    Este resultado se utilizará como caso principal de validación dentro de la aplicación.

7.  Alcance: funcionalidades que tendrá la aplicación.  
    La aplicación nos permitirá:
    Calcular la frecuencia fundamental de una columna de aire cerrada.
    Calcular armónicos impares seleccionados por el usuario.
    Determinar longitudes resonantes.
    Almacenar múltiples análisis realizados.
    Consultar el historial de cálculos.
    Mostrar estadísticas básicas del historial.
    Validar los datos ingresados por el usuario mediante menús interactivos.

8.  Comprobación de que el problema cumple todos los requisitos técnicos. 
    El problema seleccionado cumple con todos los requisitos establecidos.