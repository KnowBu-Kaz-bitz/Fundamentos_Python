# Ejercicios - Semana 1: Introducción a Python

## 📝 Instrucciones Generales

Completa estos ejercicios para reforzar los conceptos de la Semana 1. Puedes crear notebooks nuevos o archivos `.py` para cada ejercicio.

---

## ✏️ Ejercicio 1: Calculadora Básica

**Objetivo:** Practicar operadores aritméticos y uso de variables.

**Descripción:**
Crea un programa que solicite dos números al usuario y realice las siguientes operaciones:
- Suma
- Resta
- Multiplicación
- División
- División entera
- Módulo (resto)
- Potencia

**Ejemplo de salida:**
```
Ingresa el primer número: 10
Ingresa el segundo número: 3

Resultados:
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
10 // 3 = 3
10 % 3 = 1
10 ** 3 = 1000
```

**Pistas:**
- Usa `input()` para leer datos
- Convierte a número con `int()` o `float()`
- Usa f-strings para formatear la salida

---

## ✏️ Ejercicio 2: Convertidor de Unidades

**Objetivo:** Trabajar con conversiones y expresiones matemáticas.

**Descripción:**
Crea un programa que convierta:
1. Kilómetros a millas (1 km = 0.621371 millas)
2. Celsius a Fahrenheit (F = C × 9/5 + 32)
3. Kilogramos a libras (1 kg = 2.20462 libras)

El programa debe mostrar un menú para elegir la conversión.

**Ejemplo:**
```
=== Convertidor de Unidades ===
1. Kilómetros a Millas
2. Celsius a Fahrenheit
3. Kilogramos a Libras

Elige una opción: 2
Ingresa grados Celsius: 25
25°C = 77.0°F
```

---

## ✏️ Ejercicio 3: Programa de Bienvenida Personalizado

**Objetivo:** Practicar entrada/salida y concatenación de strings.

**Descripción:**
Crea un programa que:
1. Solicite el nombre del usuario
2. Solicite su edad
3. Solicite su ciudad
4. Muestre un mensaje de bienvenida personalizado
5. Calcule en qué año nacieron (aproximado)
6. Calcule cuántos días ha vivido (aproximado)

**Ejemplo:**
```
¿Cuál es tu nombre? Ana
¿Cuántos años tienes? 25
¿De qué ciudad eres? Madrid

╔════════════════════════════════╗
║   ¡BIENVENIDA ANA!            ║
╚════════════════════════════════╝

Datos:
- Edad: 25 años
- Ciudad: Madrid
- Año de nacimiento: ~2000
- Días vividos: ~9125 días

¡Nos alegra tenerte aquí! 🎉
```

**Pistas:**
- Usa `int()` para convertir la edad
- Año de nacimiento = 2025 - edad
- Días vividos ≈ edad × 365

---

## 🎯 Ejercicio Extra (Opcional): Calculadora de IMC

**Descripción:**
Crea un programa que calcule el Índice de Masa Corporal (IMC):
- IMC = peso (kg) / altura² (m)

Muestra el resultado con interpretación:
- < 18.5: Bajo peso
- 18.5 - 24.9: Normal
- 25 - 29.9: Sobrepeso
- ≥ 30: Obesidad

**Nota:** Este ejercicio requiere condicionales que veremos en la Semana 2, pero puedes intentarlo como desafío.

---

## ✅ Checklist de Completado

- [ ] Ejercicio 1: Calculadora básica
- [ ] Ejercicio 2: Convertidor de unidades
- [ ] Ejercicio 3: Programa de bienvenida
- [ ] Ejercicio Extra: Calculadora de IMC

## 📤 Entrega

Guarda tus soluciones en esta carpeta con nombres descriptivos:
- `ejercicio_1_calculadora.py`
- `ejercicio_2_convertidor.py`
- `ejercicio_3_bienvenida.py`

O crea un notebook:
- `ejercicios_semana_1.ipynb`

---

**¡Éxito con los ejercicios! 💪**
