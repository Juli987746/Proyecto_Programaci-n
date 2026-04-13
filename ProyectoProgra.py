#"""Proyecto final para nuestro curso de progra"""

# Acceso al sistema
# Inicio de sesion al sistema

usuarios_validos = ["Profesor1", "Profesor2", "Profesor3"]
password_correcta = "123"

#INICIO

def iniciosesion():
    intentos = 3
    acceso = "no"

    while intentos > 0:
        print("Bienvenido, por favor ingresa tus credenciales")
        user = input("User: ")

        if user in usuarios_validos:
            password = input("Password: ")
        
            if password == password_correcta:
                print("Acceso concedido")
                acceso = "si"
                break
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario incorrecto")
       
        intentos = intentos - 1
        print("Intentos restantes:", intentos)


    if acceso == "no":
        print("Acceso denegado")




#PRIMER MODULO - REGISTRAR ESTUDIANTES

def registroEstudiantes():
    materias = []

    cantidadMaterias= int(input("Ingrese cuántas materias desea ingresar: "))
    for i in range(cantidadMaterias):
        materia=input("Ingrese el nombre de la materia: ")
        materias.append(materia)

    estudiantes = []
    cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes que desea registrar: "))

        
    for i in range(cantidadEstudiantes):
        print("\nEstudiante", i+1)
        nombreEstudiante = input("Ingrese e nombre del estudiante:")
        estudiantes.append(nombreEstudiante)

    return materias, estudiantes
#SEGUNDO MÓDULO - Aca se registran las notas de cada estudiante 

def registroNotas(materias, estudiantes):
    matriz=[]
    promedios=[]
    estados=[]

    for estudiante in estudiantes:
        notas=[]
        total = 0
        print("Ingresa las notas de cada estudiante:")
        print()
        for materia in materias: 
            notaMateria = int(input("Ingrese la nota de " + materia + " del estudiante " + estudiante + ": "))
            notas.append(notaMateria)
            total += notaMateria
        matriz.append(notas)
        promedio = total/len(materias)
        promedios.append(promedio)

        if promedio >= 70:
            estados.append("Aprobado")
        else:
            estados.append("Reprobado")

    return matriz, estados, promedios

#TERCER MÓDULO - Este trata de consultar los estudiantes

def consultaEstudiante(matriz, estudiantes, estados, promedios):
    continuar = input("¿Desea consultar un estudiante? (si/no): ")
    while continuar == "si":
        print("\n--- Lista de estudiantes ---")
        for i in range(len(estudiantes)):
            print(i + 1, "-", estudiantes[i])

        opcion = int(input("Seleccione el número del estudiante: "))
        indice = opcion - 1
        
        print("\n--- Informe del estudiante ---")
        print("Nombre:", estudiantes[indice])
        print("Notas:")
        for nota in matriz[indice]:
            print(nota, end=" ")
        print()
        print("Promedio:", promedios[indice])
        print("Estado:", estados[indice])

        continuar = input("¿Desea consultar otro estudiante? (si/no): ")


#Cuarto y último módulo - Aca mostramos un informe general 

def informeGeneral(matriz, promedios, estados, materias, estudiantes):
    print("\n TABLA DE NOTAS \n")
    print("Estudiante\t", "\t", "\t", "\t", end="")
    for materia in materias:
        print(materia, "\t","\t", "\t", "\t", end="")
    print()
    for i in range(len(estudiantes)):
        print(estudiantes[i], "\t", "\t", "\t", "\t", end="")
        for nota in matriz[i]:
            print(nota, "\t", "\t", "\t", "\t", end="")
        print()

    for j in range(len(materias)):
        total = 0

        for i in range(len(estudiantes)):
            total += matriz[i][j]

        promedioMateria = total / len(estudiantes)

        print("Promedio general de", materias[j], ":", promedioMateria)

    mejorPromedio = 0
    nombreMejor = ""

    for i in range(len(estudiantes)):
        if promedios[i] > mejorPromedio:
            mejorPromedio = promedios[i]
            nombreMejor = estudiantes[i]

    print("Estudiante con mejor promedio:", nombreMejor)
    print("Mejor promedio:", mejorPromedio)
    print()
    print("El programa ha finalizado correctamente")


#Llamamos las funciones
iniciosesion()
materias, estudiantes = registroEstudiantes()
matriz, estados, promedios = registroNotas(materias, estudiantes)
consultaEstudiante(matriz, estudiantes, estados, promedios)
informeGeneral(matriz, promedios, estados, materias, estudiantes)

