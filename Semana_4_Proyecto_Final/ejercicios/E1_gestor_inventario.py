"""
Integrar todos los conceptos aprendidos (estructuras de datos, control de flujo, 
funciones y clases) para construir aplicaciones más complejas y estructuradas

Requisitos:

- Reutiliza la clase 'Producto' que creaste en el módulo anterior
- Crea una nueva clase 'Inventario'. El constructor de esta clase debe inicializar
un diccionario vacío para almacenar los productos
- Implementa los siguientes métodos en la clase 'Inventario':
    - 'agregar_producto(producto)': Recibe un objeto de tipo 'Producto' y lo añade
    al diccionario de inventario. Puedes usar el nombre del producto como clave
    - 'buscar_producto(nombre)': Busca un producto por su nombre y retorna el objeto 
    'Producto' si lo encuentra, o 'None' si no
    - 'generar_reporte_stock(): Itera sobre todos los productos en el inventario y 
    muestra una lista formateada del nombre de cada producto y su stock actual
- Fuera de las clases, implementa un menú principal basado en funciones para la 
interfaz de usuario. Este menú debe permitir al usuario interactuar con un objeto
'Inventario': añadir nuevos productos (creando instancias de 'Producto'), buscar
productos y ver el reporte de stock.

"""