# Calculadora con interfaz gráfica en Tkinter

### Este es un simple programa de calculadora que utiliza la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI). Permite a los usuarios realizar operaciones aritméticas básicas como suma, resta, multiplicación y división, así como exponenciación y otras funciones básicas.

## Funcionalidades

- **Operaciones básicas:** Suma, resta, multiplicación y división.
- **Exponenciación:** Permite elevar un número a una potencia.
- **Borrar y deshacer:** Los botones AC y 🠔 permiten borrar la pantalla de visualización y deshacer la última entrada, respectivamente.

## Estructura del código

El código se divide en dos clases principales:

### 1. Calculator

Esta clase contiene métodos para realizar las operaciones de la calculadora y gestionar la pantalla de visualización. Algunas de sus funciones incluyen:

- `get_numbers`: Inserta números en la pantalla de visualización.
- `get_operation`: Inserta operadores en la pantalla de visualización.
- `clear_display`: Borra el contenido de la pantalla de visualización.
- `undo`: Deshace la última entrada en la pantalla de visualización.
- `calculate`: Calcula el resultado de la expresión en la pantalla de visualización.

### 2. CalculatorApp

Esta clase es responsable de crear la interfaz gráfica de usuario utilizando Tkinter. Define la disposición de los widgets y vincula los botones a los métodos de la clase Calculator.

## Uso

Para ejecutar la calculadora, simplemente ejecuta el script `calculator_app.py`. Se abrirá una ventana con la interfaz de la calculadora, donde puedes realizar operaciones aritméticas básicas.
