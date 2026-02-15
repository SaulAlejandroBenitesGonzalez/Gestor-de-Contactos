import sys  # Import una vez arriba

def main():
    contactos = {'saul': '4761638198', 'brisa': '478569215'}
    
    opciones = {
        '1': agregar,
        '2': buscar,
        '3': mostrar_todos_los_contactos,
        '4': eliminar_contactos,
        '5': salir
    }
    
    while True:
        mostrar_menu()
        opcion = input("Qué deseas hacer: ").strip()
        
        if opcion in opciones:
            if opcion in ['1', '2', '3', '4']:
                opciones[opcion](contactos)
            else:
                opciones[opcion]()
        else:
            print("Opción inválida, intenta de nuevo.")

def mostrar_menu():
    print("\n______________Menú_____________________")
    print("1.- Agregar contacto")
    print("2.- Buscar contacto")
    print("3.- Mostrar todos los contactos")
    print("4.- Eliminar contacto")
    print("5.- Salir")

def agregar(contactos):
    nombre = input("Ingresa el nombre: ").strip()
    if nombre in contactos:
        print("¡Contacto duplicado! No se agregó.")
        return
    
    telefono = input("Ingresa el número de teléfono: ").strip()
    contactos[nombre] = telefono
    print(f"El contacto {nombre} fue agregado con éxito.")

def buscar(contactos):
    nombre = input("Ingresa el nombre del contacto: ").strip()
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print("No existe ese contacto.")

def mostrar_todos_los_contactos(contactos):
    if not contactos:
        print("Aún no hay contactos.")
        return
    print("\n---------- Contactos en orden alfabético ----------")
    for nombre in sorted(contactos.keys()):
        print(f"{nombre}: {contactos[nombre]}")
    print("---------------------------------------------------")

def eliminar_contactos(contactos):
    nombre = input("Ingresa el nombre del contacto a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print("No existe ese contacto.")

def salir():
    print("¡Bonito día! Bye ;3")
    sys.exit()

if __name__ == "__main__":
    main()