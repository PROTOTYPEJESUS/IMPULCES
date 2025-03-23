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

    users[email] = {"name": name, "lastname": lastname, "password": password, "grades": {}}
    print("Usuario registrado con éxito.\n")

# FUNCION PARA INICIAR SESION
def login():
    print("\n--- INICIAR SESIÓN EN IMPULCES NOTAS ---")
    
    for _ in range(3):  # Permitir hasta 3 intentos de verificacion
        email = input("Ingrese correo electrónico: ").strip()
        password = input("Ingrese contraseña: ").strip()

        if email in users and users[email]["password"] == password:
            print(f"Bienvenido, {users[email]['name']} {users[email]['lastname']}.\n")
            return True  # Usuario autenticado y devuelve nombre completo

        print("Usuario o contraseña incorrectos. Intente nuevamente.\n")

    print("Demasiados intentos fallidos. Intente más tarde.\n")
    return False  # Inicio de sesión fallido

# PRUEBA
register_user()
login()
