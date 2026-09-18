import time
from datos import cargar_datos, guardar_datos
from operaciones import (mostrar_inventario, agregar_elemento, 
                         buscar_elemento, editar_elemento, 
                         eliminar_elemento, filtrar_por_conferencia)

# Estudiante: Manuel 
# Grupo: UTNG
# Descripción: Inventario de Equipos de la NBA

def mostrar_menu():
    print("\n" + "="*27)
    print("  SISTEMA DE INVENTARIO: EQUIPOS DE LA NBA ")
    print("="*27)
    print(" 1. Agregar nuevo equipo")
    print(" 2. Mostrar todos los equipos registrados")
    print(" 3. Buscar un equipo por nombre o código")
    print(" 4. Editar los campeonatos de un equipo")
    print(" 5. Eliminar un equipo del sistema")
    print(" 6. Filtrar equipos por conferencia")
    print(" 7. Guardar y Salir")
    print(" 8. Salir sin Guardar")
    print("="*27)

def main():
    inventario = cargar_datos()
    while True:
        time.sleep(1)
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        match opcion:
            case '1':
                agregar_elemento(inventario)
            case '2':
                mostrar_inventario(inventario)
            case '3':
                buscar_elemento(inventario)
            case '4':
                editar_elemento(inventario)
            case '5':
                eliminar_elemento(inventario)
            case '6':
                filtrar_por_conferencia(inventario)
            case '7':
                guardar_datos(inventario)
                print("Inventario guardado. Saliendo del sistema...")
                break
            case '8':
                print("Saliendo del programa sin guardar.")
                break
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()