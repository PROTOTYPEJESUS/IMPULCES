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

# Menu principal
def main_menu():
    while True:
        print("\n--- BIENVENIDO AL SISTEMA DE REGISTRO DE NOTAS DE IMPULCES ---")
        print("\n--- MENU PRINCIPAL ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        option = input("Elija una opción: ")

        if option == "1":
            register_user()
        elif option == "2":
            login()
        elif option == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

# Datos de prueba
users = {
    "profesor1@email.com": {
        "name": "Carlos",
        "lastname": "Gómez",
        "password": "profesor123",
        "role": "profesor",
        "grades": {} 
    },
    "estudiante1@email.com": {
        "name": "Ana",
        "lastname": "Pérez",
        "password": "estudiante123",
        "role": "estudiante",
        "grades": {
            "Matemáticas": 85,
            "Historia": 90
        }
    }
}

# FUNCION PARA AGREGAR NOTAS (Solo profesores)
def add_grades():
    print("\n--- AGREGAR NOTAS ---")

    student_email = input("Ingrese el correo del estudiante: ").strip()
    if student_email not in users or users[student_email]["role"] != "estudiante":
        print("Este usuario no es un estudiante registrado.")
        return

    subject = input("Ingrese la materia: ").strip()
    while True:
        try:
            grade = float(input("Ingrese la nota (0-5): ").strip())
            if 0 <= grade <= 5:
                break
            else:
                print("La nota debe estar entre 0 y 5.")
        except ValueError:
            print("Ingrese un número válido.")

    users[student_email]["grades"][subject] = grade
    print(f"Nota agregada exitosamente para {users[student_email]['name']}.")

# FUNCION PARA VER NOTAS
def view_grades(user_email):
    user = users[user_email]
    print(f"\n--- NOTAS DE {user['name']} {user['lastname']} ---")

    if user["grades"]:
        for subject, grade in user["grades"].items():
            print(f"{subject}: {grade}")
    else:
        print("No hay notas registradas.")


# LANZAR EL SISTEMA
main_menu()