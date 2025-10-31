"""
Integrar todos los conceptos aprendidos (estructuras de datos, control de flujo, 
funciones y clases) para construir aplicaciones más complejas y estructuradas

Requisitos:

- Define una clase llamada 'Libro', con los atributos 'titulo', 'autor' y un
booleano 'prestado' (inicialmente False)
- Define una clase 'Biblioteca' que gestionará toda la lógica. Su constructor 
debe inicializar una lista vacía para almacenar los objetos 'Libro'
- Implementa los siguientes métodos:
    - 'agregar_libro(libro)': añade un objeto 'Libro' a la lista de la biblioteca
    - 'mostrar_libros_disponibles(): itera sobre la lista de libros y muestra 
    solo aquellos cuyo atributo 'prestado' sea 'False'
    - 'prestar_libro(titulo)': busca un libro por su titulo. Si existe y no está 
    prestado, cambia su atributo 'prestado' a 'True'. Si ya está prestado o no 
    existe, informa al usuario
    - 'devolver_libro(titulo)': busca un libro por su titulo y, si existe, cambia 
    su atributo 'prestado' a 'False'
- Crea un menú de usuario con funciones para interactuar con la biblioteca: agregar 
un nuevo libro, ver los disponibles, prestar uno y devolverlo

"""