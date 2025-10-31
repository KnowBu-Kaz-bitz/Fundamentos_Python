"""
Profundizar en el uso de diccionarios, incluyendo diccionarios anidados, para gestionar
una colección de datos estructurados

Requsitos:

- Crea un diccionario vacío que funcionará como tu agenda.
- La clave de cada entrada será el nombre del contacto (un string).
- El valor será otro diccionario con los detalles del contacto: {"telefono": "...", "email": "..."}.
- Implementa un menú interactivo con un bucle while y las siguientes opciones:
    - 1. Agregar/Modificar Contacto: Pide un nombre, teléfono y email. Si el nombre ya existe, actualiza sus datos. Si no, lo crea.
    - 2. Buscar Contacto: Pide un nombre y, si existe, muestra sus detalles. Si no, informa que no se encontró.
    - 3. Eliminar Contacto: Pide un nombre y, si existe, lo borra de la agenda.
    - 4. Ver todos los contactos: Itera sobre el diccionario y muestra la información de todos los contactos.
    - 5. Salir.
"""