# Ejercicios - Semana 3: Funciones y Módulos

## 📝 Instrucciones Generales

Estos ejercicios te ayudarán a crear código modular y reutilizable.

---

## ✏️ Ejercicio 1: Calculadora con Funciones

**Objetivo:** Crear funciones reutilizables.

**Descripción:**
Refactoriza la calculadora de la Semana 1 usando funciones:
- `sumar(a, b)`
- `restar(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)` (con manejo de división por cero)

Crea un menú que llame a estas funciones.

---

## ✏️ Ejercicio 2: Validador de Datos

**Objetivo:** Practicar manejo de errores.

**Descripción:**
Crea funciones para validar:
1. Email (contiene @ y .)
2. Teléfono (10 dígitos)
3. Edad (entre 0 y 120)
4. Contraseña (mínimo 8 caracteres)

Usa try-except para manejar errores.

---

## ✏️ Ejercicio 3: Sistema de Módulos - Inventario

**Objetivo:** Organizar código en módulos.

**Descripción:**
Crea un sistema de inventario con 3 módulos:
- `productos.py`: Funciones CRUD de productos
- `reportes.py`: Generar reportes
- `main.py`: Programa principal

---

## ✏️ Ejercicio 4: Funciones de Orden Superior

**Objetivo:** Usar map, filter, reduce.

**Tareas:**
1. Usa `map()` para convertir lista de strings a mayúsculas
2. Usa `filter()` para filtrar números positivos
3. Usa `reduce()` para calcular factorial
4. Crea tu propia función de orden superior

---

## ✏️ Ejercicio 5: Decorador de Tiempo

**Objetivo:** Crear un decorador.

**Descripción:**
Crea un decorador que mida y muestre el tiempo de ejecución de funciones.

**Ejemplo:**
```python
@medir_tiempo
def operacion_lenta():
    # código
    pass

# Salida: "Función ejecutada en 2.34 segundos"
```

---

## ✅ Checklist de Completado

- [ ] Ejercicio 1: Calculadora con funciones
- [ ] Ejercicio 2: Validador de datos
- [ ] Ejercicio 3: Sistema de módulos
- [ ] Ejercicio 4: Map, filter, reduce
- [ ] Ejercicio 5: Decorador de tiempo

---

**¡Excelente progreso! 🎯**
