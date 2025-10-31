"""
Practicar la combinación de bucles while con múltiples condicionales if/elif/else
para crear un programa interactivo que mantiene un estado ("el saldo")

Requsitos:

- Inicia una variable "saldo" con un valor inicial
- Crea un bucle while True para el programa se ejecute continuamente hasta
que el usuario decida salir
- Dentro del bucle, muestra un menú de opciones:
    - 1. Consultar Saldo
    - 2. Depositar dinero
    - 3. Retirar dinero
    - 4. Salir
- Según la elección del usuario, se ejecuta la acción correspondiente:
     - Depositar: Pide una cantidad al usuario y la suma con el saldo actual y muestra el nuevo saldo
     - Retirar: Pide una cantidad a retirar. Verifica si hay fondos suficientes. Si los hay, resta la cantidad del
     saldo actual y muestra el nuevo saldo. Si no hay fondos suficientes, muestra un mensaje de error
    - Salir: Interrumpe el bucle con break
"""