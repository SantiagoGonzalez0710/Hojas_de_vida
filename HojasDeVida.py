# Sistema de Información para perfilar hojas de vida

ofertas = []
candidatos = []

def registrar_oferta():
    titulo = input("Título del puesto: ")
    empresa = input("Empresa: ")
    descripcion = input("Descripción: ")
    ofertas.append({"titulo": titulo, "empresa": empresa, "descripcion": descripcion})
    print("Oferta registrada.\n")

def registrar_candidato():
    nombre = input("Nombre completo: ")
    perfil = input("Perfil profesional: ")
    experiencia = input("Años de experiencia: ")
    candidatos.append({"nombre": nombre, "perfil": perfil, "experiencia": experiencia})
    print("Hoja de vida registrada.\n")

def mostrar_ofertas():
    print("Ofertas laborales registradas:")
    for o in ofertas:
        print(o)

def mostrar_candidatos():
    print("Candidatos registrados:")
    for c in candidatos:
        print(c)

def agregar_perfil_laboral():
    nombre = input("Nombre del candidato: ")
    nuevo_perfil = input("Nuevo perfil laboral: ")
    for c in candidatos:
        if c["nombre"] == nombre:
            c["perfil"] = nuevo_perfil
            print("Perfil actualizado.\n")
            return
    print("Candidato no encontrado.\n")

def menu():
    while True:
        print("\nMenú")
        print("1. Registrar oferta laboral")
        print("2. Registrar candidato")
        print("3. Mostrar ofertas")
        print("4. Mostrar candidatos")
        print("5. Agregar perfil laboral")
        print("6. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            registrar_oferta()
        elif opcion == "2":
            registrar_candidato()
        elif opcion == "3":
            mostrar_ofertas()
        elif opcion == "4":
            mostrar_candidatos()
        elif opcion == "5":
            agregar_perfil_laboral()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

menu()