# VARIABLES DE ALMACENAMIENTO EN DICCIONARIOS

users = {} # Diccionario para almacenar usuarios

# FUNCION PARA REGISTRAR USUARIOS
def register_user():
    print("\n--- BIENVENIDO AL SISTEMA DE REGISTRO DE NOTAS DE IMPULCES ---")
    
    while True:
        email = input("Ingrese correo electrónico: ").strip()
        if not email:
            print("El correo electrónico no puede estar vacío.")
            continue
        if email in users:
            print("Este correo ya está registrado. Intente con otro.\n")
            return
        break

    while True:
        name = input("Ingrese su primer nombre: ").strip()
        if name:
            break
        print("El nombre no puede estar vacío.")

    while True:
        lastname = input("Ingrese su primer apellido: ").strip()
        if lastname:
            break
        print("El apellido no puede estar vacío.")

    while True:
        password = input("Ingrese contraseña: ").strip()
        if password:
            break
        print("La contraseña no puede estar vacía.")

    while True:
        role = input("Ingrese su rol (profesor/estudiante): ").strip().lower()
        if role in ["profesor", "estudiante"]:
            break
        print("El rol debe ser 'profesor' o'estudiante'.")

    users[email] = {"name": name, "lastname": lastname, "password": password, "role": role, "grades": {}}
    print("Usuario registrado con éxito.\n")