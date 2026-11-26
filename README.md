Nombre: María Fernanda Hernández Avalos

Descripción:
Este proyecto consiste en una aplicación de consola desarrollada en Python para analizar fenómenos de resonancia en columnas de aire cerradas.
El programa se basa en un problema estudiado previamente en la materia de Física I, donde se calcula la frecuencia fundamental y los armónicos 
de una columna de aire a partir de su longitud y la velocidad del sonido.
La aplicación fue desarrollada utilizando programación orientada a objetos y siguiendo una metodología basada en análisis, especificaciones, 
implementación, pruebas y documentación.

Asignatura Original: Física I

Objetivo:
Desarrollar una aplicación capaz de calcular frecuencias resonantes en columnas de aire cerradas, permitiendo almacenar resultados y realizar 
consultas mediante un menú interactivo.

Funcionalidades:
Calcular la frecuencia fundamental.
Calcular armónicos impares.
Mostrar historial de frecuencias calculadas.
Calcular el promedio de frecuencias registradas.
Obtener la frecuencia máxima registrada.
Validar entradas incorrectas.
Gestionar la información mediante programación orientada a objetos.

Clases:
TuboResonante: Representa una columna de aire cerrada y realiza los cálculos físicos relacionados con la resonancia.
Métodos principales:
    calcular_fundamental()
    calcular_armonico()
    mostrar_resultados()

HistorialResonancias: Administra el almacenamiento y consulta de frecuencias calculadas.
Métodos principales:
    agregar_resultado()
    mostrar_historial()
    calcular_promedio()
    obtener_maximo()

Requisitos:

Instalaciones:

Instrucciones de ejecución:

Ejemplo:
Datos de entrada
    Longitud = 0.09 m
    Velocidad del sonido = 343 m/s
    Resultado: Frecuencia fundamental = 952.78 Hz
Este resultado coincide con el ejercicio original utilizado para validar el proyecto.

1.  ¿Cómo utilizaste las especificaciones para solicitar código a Copilot? 
    Primero elaboré las especificaciones de las clases y del programa principal antes de comenzar a programar. 
    En las especificaciones definí el objetivo de cada clase, sus atributos, el constructor, los métodos y las 
    validaciones necesarias. Posteriormente utilicé esas especificaciones como guía para solicitar a Copilot la 
    implementación de cada clase por separado, siguiendo la metodología indicada en la rúbrica. De esta manera, 
    Copilot funcionó como una herramienta de apoyo para generar código a partir de un diseño previamente definido.

2.  ¿Qué revisaste o modificaste del código generado? 
    Revisé que los nombres de las clases, atributos y métodos coincidieran con los definidos en las especificaciones. 
    También comprobé que las fórmulas físicas utilizadas para calcular la frecuencia fundamental y los armónicos fueran 
    correctas. Además, agregué y ajusté validaciones para impedir longitudes negativas, velocidades menores o iguales a 
    cero y armónicos no permitidos. Finalmente, simplifiqué algunas partes del código para que fueran más fáciles de entender 
    y explicar durante la revisión del proyecto.

3.  ¿Copilot generó una respuesta incorrecta o distinta de lo solicitado? Explica un caso si ocurrió.
    Sí. Durante el desarrollo surgieron situaciones en las que fue necesario revisar y ajustar el código generado. Por ejemplo, 
    fue necesario verificar que el programa rechazara valores inválidos como longitudes negativas o armónicos pares. Después de 
    realizar pruebas, se agregaron validaciones adicionales para asegurar que el comportamiento del programa coincidiera con las 
    reglas físicas del problema. Este proceso permitió comprobar la importancia de revisar cuidadosamente el código generado y no 
    aceptarlo sin analizarlo.

4.  ¿Cómo comprobaste el funcionamiento de clases y métodos? 
    Primero probé cada clase por separado para verificar que sus métodos funcionaran correctamente. Después integré las clases dentro 
    del menú principal y ejecuté diferentes casos de prueba. También comparé el resultado del caso original de Física I con el resultado 
    obtenido por el programa. Finalmente, ejecuté pruebas adicionales con valores válidos e inválidos para verificar las validaciones implementadas.

5.  ¿Qué ventajas y limitaciones observaste? 
    Una ventaja importante es que Copilot ayuda a acelerar la escritura del código y proporciona sugerencias útiles para implementar clases 
    y métodos. También facilita la detección de errores simples y propone estructuras de programación. Como limitación, observé que las 
    sugerencias deben revisarse cuidadosamente porque no siempre consideran todas las reglas específicas del problema. Por esta razón, fue necesario 
    validar resultados y realizar ajustes manuales.

6.  ¿Por qué es necesario comprender código producido con ayuda de IA?
    Es necesario comprender el código porque el estudiante sigue siendo responsable del funcionamiento de la aplicación. 
    Aunque la IA pueda generar sugerencias, únicamente el programador puede verificar si las fórmulas, validaciones y decisiones implementadas 
    corresponden correctamente al problema que se desea resolver. Además, comprender el código permite explicar su funcionamiento, realizar 
    modificaciones y detectar posibles errores.
    