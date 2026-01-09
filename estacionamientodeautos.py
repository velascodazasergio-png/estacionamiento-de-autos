capacidad_maxima = 20
autos_actuales = 0
# menú de inicio
while True:
    print("/////////////////////////////////////////")
    print("/------ Estacionamiento de autos ------/")
    print("1. Registro de autos que entran")
    print("2. Retirar auto")
    print("3. Mostrar espacios disponibles")
    print("4. Salir")
    print("/////////////////////////////////////////")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if autos_actuales < capacidad_maxima:
            autos_actuales += 1
            print("Auto ingresado correctamente.")
        else:
            print("Estacionamiento lleno.")

    elif opcion == "2":
        if autos_actuales > 0:
            autos_actuales -= 1
            print("Auto retirado correctamente.")
        else:
            print("No hay autos para retirar.")

    elif opcion == "3":
        espacios_disponibles = capacidad_maxima - autos_actuales
        print(f"Espacios disponibles: {espacios_disponibles}")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
