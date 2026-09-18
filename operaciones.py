import time
from tabulate import tabulate

def mostrar_inventario(data):
    if not data:
        print("El inventario de equipos está vacío.")
        return
    print("\n" + tabulate(data, headers="keys", tablefmt="grid"))

def agregar_elemento(data):
    while True:
        codigo = input("Ingrese la abreviatura del equipo (Ej. LAL, BOS): ").strip().upper()
        if codigo: break
        print("El código no puede estar vacío.")
        
    while True:
        nombre = input("Ingrese el nombre completo del equipo: ").strip()
        if nombre: break
        print("El nombre no puede estar vacío.")

    while True:
        try:
            campeonatos = int(input("Ingrese el número de campeonatos ganados: "))
            break
        except ValueError:
            print("Error: la cantidad debe ser un número entero.")

    conferencias_validas = ["Este", "Oeste"]
    while True:
        print(f"Conferencias válidas: {', '.join(conferencias_validas)}")
        conferencia = input("Ingrese la conferencia: ").strip().capitalize()
        if conferencia in conferencias_validas: break
        print("Conferencia no válida. Intente de nuevo.")

    while True:
        estadio = input("Ingrese el nombre del estadio: ").strip()
        if estadio: break
        print("El estadio no puede estar vacío.")

    equipo = {
        'codigo': codigo,
        'nombre': nombre,
        'campeonatos': campeonatos,
        'conferencia': conferencia,
        'estadio': estadio
    }
    data.append(equipo)
    print("\nEquipo de la NBA agregado exitosamente.")
    time.sleep(1)

def buscar_elemento(inventario):
    dato = input("Ingrese el código o nombre a buscar: ").strip()
    encontrado = False
    resultados = []
    
    for elemento in inventario:
        if dato.lower() in elemento["codigo"].lower() or dato.lower() in elemento["nombre"].lower():
            resultados.append(elemento)
            encontrado = True
            
    if not encontrado:
        print("No se encontró ningún equipo con ese dato.")
    else:
        print("\n" + tabulate(resultados, headers="keys", tablefmt="grid"))
    time.sleep(1)

def editar_elemento(inventario):
    codigo = input("Ingrese el código del equipo a editar (Ej. LAL): ").strip().upper()
    for elemento in inventario:
        if elemento["codigo"] == codigo:
            try:
                nueva_cantidad = int(input(f"Campeonatos actuales ({elemento['campeonatos']}). Nuevos campeonatos: "))
                elemento["campeonatos"] = nueva_cantidad
                print("Campeonatos del equipo actualizados.")
                time.sleep(1)
                return
            except ValueError:
                print("Error: la cantidad debe ser un número entero.")
                return
    print("No se encontró un equipo con ese código.")

def eliminar_elemento(inventario):
    codigo = input("Ingrese el código del equipo a eliminar: ").strip().upper()
    for elemento in inventario:
        if elemento["codigo"] == codigo:
            inventario.remove(elemento)
            print("Equipo eliminado del inventario.")
            time.sleep(1)
            return
    print("No se encontró un equipo con ese código.")

def filtrar_por_conferencia(inventario):
    conferencia = input("Ingrese la conferencia a filtrar (Este, Oeste): ").strip().capitalize()
    resultados = [elem for elem in inventario if elem["conferencia"] == conferencia]
    if resultados:
        print("\n" + tabulate(resultados, headers="keys", tablefmt="grid"))
    else:
        print(f"No hay equipos registrados en la conferencia: {conferencia}")
    time.sleep(1)