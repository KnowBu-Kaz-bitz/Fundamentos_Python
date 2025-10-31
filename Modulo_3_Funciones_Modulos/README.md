# Semana 3: Funciones y Módulos

## Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Definir y usar funciones personalizadas
- ✅ Trabajar con parámetros, argumentos y valores de retorno
- ✅ Comprender el scope (ámbito) de las variables
- ✅ Usar funciones lambda y funciones de orden superior
- ✅ Organizar código en módulos y paquetes
- ✅ Manejar errores y excepciones apropiadamente

## Contenido

### Notebook 1: Funciones
- Definición de funciones (def)
- Parámetros y argumentos
- Valores de retorno (return)
- Argumentos por defecto
- *args y **kwargs
- Docstrings y documentación
- Funciones como objetos

### Notebook 2: Scope y Funciones Avanzadas
- Scope local, global y nonlocal
- Funciones lambda (anónimas)
- Funciones de orden superior (map, filter, reduce)
- Decoradores básicos
- Recursividad
- Closures

### Notebook 3: Módulos y Manejo de Errores
- Importar módulos (import)
- Crear módulos personalizados
- Paquetes y __init__.py
- Módulos de la biblioteca estándar
- Try-except-finally
- Tipos de excepciones
- Raise y excepciones personalizadas

## Ejercicios

Los ejercicios de esta semana se encuentran en la carpeta `ejercicios/`:

1. **Ejercicio 1:** Calculadora con funciones
2. **Ejercicio 2:** Validador de datos (manejo de errores)
3. **Ejercicio 3:** Sistema de módulos para gestión de inventario
4. **Ejercicio 4:** Funciones de orden superior aplicadas
5. **Ejercicio 5:** Decorador para medir tiempo de ejecución

## Material de Apoyo

- **Presentación:** `presentaciones/Semana3_Funciones_Modulos.pdf`
- **Datos de práctica:** `datos/` (módulos de ejemplo)

## Recursos Adicionales

- [Funciones en Python](https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions)
- [Módulos en Python](https://docs.python.org/es/3/tutorial/modules.html)
- [Errores y excepciones](https://docs.python.org/es/3/tutorial/errors.html)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

## ⏱Tiempo Estimado

- **Lectura y práctica:** 6-8 horas
- **Ejercicios:** 4-5 horas
- **Total:** 10-13 horas

## ✅ Checklist de la Semana

- [ ] Puedo definir funciones con diferentes tipos de parámetros
- [ ] Entiendo el concepto de scope
- [ ] Sé usar funciones lambda y map/filter
- [ ] Puedo crear y usar módulos personalizados
- [ ] Comprendo el manejo de excepciones con try-except
- [ ] He completado todos los ejercicios

## Conceptos Clave

```python
# Función básica
def saludar(nombre, saludo="Hola"):
    """Saluda a una persona."""
    return f"{saludo}, {nombre}!"

# Lambda
cuadrado = lambda x: x**2

# Manejo de errores
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Operación completada")

# Módulo
import math
print(math.pi)
```

## Buenas Prácticas

1. **Funciones pequeñas:** Una función debe hacer una cosa y hacerla bien
2. **Nombres descriptivos:** `calcular_promedio()` es mejor que `calc()`
3. **Documenta tu código:** Usa docstrings
4. **Maneja errores:** Prevé situaciones excepcionales
5. **DRY:** Don't Repeat Yourself - reutiliza código

## Próximos Pasos

¡Estás casi listo! La próxima semana aplicarás todo lo aprendido en la [Semana 4: Proyecto Final](../Semana_4_Proyecto_Final/), donde construirás una aplicación completa.

---

**Recuerda:** La práctica hace al maestro. Experimenta creando tus propias funciones y módulos.
