# ============================================
# ORGANIZADOR INTELIGENTE DE TAREAS
# Mini Proyecto - Python Básico
# ============================================

from datetime import datetime


# --------------------------------------------
# DATOS INICIALES
# --------------------------------------------
tareas = [
    {
        'id': 1,
        'titulo': 'Estudiar Python',
        'prioridad': 'alta',
        'categoria': 'estudio',
        'fecha_limite': '2025-11-25',
        'completada': False
    },
    {
        'id': 2,
        'titulo': 'Reunion de equipo',
        'prioridad': 'media',
        'categoria': 'trabajo',
        'fecha_limite': '2025-11-22',
        'completada': False
    },
    {
        'id': 3,
        'titulo': 'Hacer ejercicio',
        'prioridad': 'baja',
        'categoria': 'personal',
        'fecha_limite': '2025-11-19',
        'completada': True
    }
]

contador_id = 4


# --------------------------------------------
# FUNCIONES
# --------------------------------------------

def agregar_tarea():
    """Agrega una nueva tarea."""
    global contador_id
    
    print("\n--- AGREGAR NUEVA TAREA ---")
    titulo = input("Titulo: ")
    prioridad = input("Prioridad (alta/media/baja): ")
    categoria = input("Categoria (trabajo/estudio/personal): ")
    fecha_limite = input("Fecha limite (YYYY-MM-DD): ")
    
    nueva_tarea = {
        'id': contador_id,
        'titulo': titulo,
        'prioridad': prioridad,
        'categoria': categoria,
        'fecha_limite': fecha_limite,
        'completada': False
    }
    
    tareas.append(nueva_tarea)
    print(f"\nTarea agregada con ID: {contador_id}")
    contador_id += 1


def mostrar_tareas():
    """Muestra todas las tareas."""
    print("\n--- TODAS LAS TAREAS ---")
    
    if len(tareas) == 0:
        print("No hay tareas.")
        return
    
    for tarea in tareas:
        estado = "COMPLETADA" if tarea['completada'] else "PENDIENTE"
        print(f"\nID: {tarea['id']}")
        print(f"Titulo: {tarea['titulo']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Categoria: {tarea['categoria']}")
        print(f"Fecha limite: {tarea['fecha_limite']}")
        print(f"Estado: {estado}")


def marcar_completada():
    """Marca una tarea como completada."""
    print("\n--- MARCAR COMO COMPLETADA ---")
    
    try:
        id_tarea = int(input("Ingrese el ID de la tarea: "))
        
        for tarea in tareas:
            if tarea['id'] == id_tarea:
                tarea['completada'] = True
                print(f"\nTarea '{tarea['titulo']}' completada!")
                return
        
        print("\nTarea no encontrada.")
    
    except:
        print("\nError: Ingrese un numero valido.")


def filtrar_por_categoria():
    """Filtra tareas por categoria."""
    print("\n--- FILTRAR POR CATEGORIA ---")
    categoria = input("Categoria (trabajo/estudio/personal): ")
    
    print(f"\nTareas de categoria '{categoria}':")
    encontradas = 0
    
    for tarea in tareas:
        if tarea['categoria'] == categoria:
            estado = "COMPLETADA" if tarea['completada'] else "PENDIENTE"
            print(f"- [ID: {tarea['id']}] {tarea['titulo']} - {estado}")
            encontradas += 1
    
    if encontradas == 0:
        print("No hay tareas en esta categoria.")


def tareas_vencidas():
    """Muestra tareas vencidas."""
    print("\n--- TAREAS VENCIDAS ---")
    
    fecha_actual = datetime.now().date()
    vencidas = 0
    
    for tarea in tareas:
        try:
            fecha_limite = datetime.strptime(tarea['fecha_limite'], '%Y-%m-%d').date()
            if fecha_limite < fecha_actual and not tarea['completada']:
                print(f"- [ID: {tarea['id']}] {tarea['titulo']} - Vencio: {tarea['fecha_limite']}")
                vencidas += 1
        except:
            print(f"Error en fecha de tarea ID {tarea['id']}")
    
    if vencidas == 0:
        print("No hay tareas vencidas.")


def estadisticas():
    """Muestra estadisticas de las tareas."""
    print("\n--- ESTADISTICAS ---")
    
    total = len(tareas)
    completadas = 0
    pendientes = 0
    alta = 0
    media = 0
    baja = 0
    
    for tarea in tareas:
        if tarea['completada']:
            completadas += 1
        else:
            pendientes += 1
        
        if tarea['prioridad'] == 'alta':
            alta += 1
        elif tarea['prioridad'] == 'media':
            media += 1
        elif tarea['prioridad'] == 'baja':
            baja += 1
    
    print(f"\nTotal de tareas: {total}")
    print(f"Completadas: {completadas}")
    print(f"Pendientes: {pendientes}")
    print(f"\nPor prioridad:")
    print(f"  Alta: {alta}")
    print(f"  Media: {media}")
    print(f"  Baja: {baja}")


def menu():
    """Muestra el menu principal."""
    print("\n" + "=" * 40)
    print("    ORGANIZADOR DE TAREAS")
    print("=" * 40)
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar como completada")
    print("4. Filtrar por categoria")
    print("5. Ver tareas vencidas")
    print("6. Ver estadisticas")
    print("7. Salir")
    print("=" * 40)
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
        
        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            mostrar_tareas()
        elif opcion == 3:
            marcar_completada()
        elif opcion == 4:
            filtrar_por_categoria()
        elif opcion == 5:
            tareas_vencidas()
        elif opcion == 6:
            estadisticas()
        elif opcion == 7:
            print("\nGracias por usar el organizador!")
            return False
        else:
            print("\nOpcion invalida.")
    
    except:
        print("\nError: Ingrese un numero valido.")
    
    return True


# --------------------------------------------
# EJECUCIÓN PRINCIPAL
# --------------------------------------------

if __name__ == "__main__":
    continuar = True
    
    for i in range(100):  # Limite de 100 iteraciones
        if continuar:
            continuar = menu()
        else:
            break
    
    print("\nHasta pronto!\n")