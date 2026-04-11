""""
Establecemos el menu del restaurante

"""

def mostrarmenu():
    menu = []

    menu.append(["Hamburguesa", 3500])
    menu.append(["Pizza", 5000])
    menu.append(["Pasta", 4200])
    menu.append(["Ensalada", 3000])
    menu.append(["Sushi", 6000])

    return menu

def mostrar_menu(menu):
    print("\n--- MENU ---\n")

    i = 0
    while i < 5:
        fila = menu[i]
        nombreplato = fila[0]
        precio = fila[1]

        print(i+1, "-", nombreplato, precio)
        i = i + 1

menu = mostrarmenu()

total_dia = 0
cantidad_reservas = 0
continuar = "si"

while continuar == "si":

    mostrar_menu(menu)


# Dia
    dia = input("\nDia: ")
    while dia != "martes" and dia != "miercoles" and dia != "miércoles" and dia != "jueves" and dia != "viernes" and dia != "sabado" and dia != "domingo":
        print("Digitaste un dia en el que el servicio no esta disponible")
        dia = input("Dia: ").lower()

# Tipo de servicio

tiposervicio = 0
while tiposervicio != 1 and tiposervicio != 2 and tiposervicio != 3:
    print("\n1. Mesa\n2. Llevar\n3. Express")
    tiposervicio = int(input("Tipo: "))
    if tiposervicio != 1 and tiposervicio != 2 and tiposervicio != 3:
            print("Digitaste un numero de servicio que no esta disponible")

# Cantidad personas en la reservacion

personas = 0
while personas < 1 or personas > 10:
    personas = int(input("\nPersonas: "))
    if personas < 1 or personas > 10:
        print("Digitaste una cantidad mayor de la admitida en el sistama")


factura = 0

i = 0
while i < personas:
    print("\nPersona: ",i+1)

    nombre = input("Nombre: ")
    telefono = input("Telefono: ")

    # Platillo a elegir
    opcionplatillo = 0
    while opcion < 1 or opcion > 5:
        opcionplatillo = int(input("Elige una opcion del menu, ya sea 1,2,3,4,5: "))
        if opcionplatillo <5:
            print("Digitaste una opcion del menu que no esta disponible")

    fila = menu[opcionplatillo - 1]
    platillo = fila[0]
    precio = fila[1]

    total = precio * 1.13

    if tiposervicio == 2:
        total = total + 500
    elif tiposervicio == 3:
        total = total + 1500

    factura += total

    print("\nResumen reservacion:")
    print("Nombre:", nombre)
    print("Telefono:", telefono)
    print("Platillo:", platillo)
    print("Precio:", precio)
    print("Total:", total)

    i = i + 1

    # AJUSTE POR DIA
    if dia == "viernes" or dia == "sabado" or dia == "sábado":
        total_reserva = total_reserva * 1.10
    elif dia == "martes" or dia == "miercoles" or dia == "miércoles" or dia == "jueves":
        total_reserva = total_reserva * 0.95

    print("\nel total de la reserva sera :", total_reserva)

    total_dia = total_dia + total_reserva
    cantidad_reservas = cantidad_reservas + 1

    continuar = input("\ndeseas ingresar otra reserva? (si/no): ")


# FINAL
print("\n--- Resumen reservas hechas el dia de hoy ---")
print("Reservas totales:", cantidad_reservas)

if cantidad_reservas > 0:
    promedio = total_dia / cantidad_reservas
else:
    promedio = 0

print("Total:", total_dia)
print("Promedio:", promedio)

