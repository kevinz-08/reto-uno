import random
import string

# Función para generar la contraseña segura según las preferencias del usuario
def generarcontraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    # Inicializar conjunto de caracteres permitidos según las opciones del usuario
    caracteres = ''

    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Debes seleccionar al menos un tipo de carácter (mayúsculas, minúsculas, números, símbolos)."

    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Función para mostrar el menú y obtener la entrada del usuario
def mostrar_menu():
    print("\nGenerador de Contraseñas Seguras")
    print("Seleccione las opciones que desea para su contraseña:")

    longitud = int(input("1. Longitud de la contraseña: "))
    incluir_mayusculas = input("2. Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("3. Incluir minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("4. Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("5. Incluir símbolos? (s/n): ").lower() == 's'

    # Generar la contraseña según las preferencias
    contraseña = generarcontraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    print(f"\nContraseña generada: {contraseña}")

# Función principal que controla la interacción con el usuario
def main():
    print("Bienvenido al generador de contraseñas seguras.")
    print("Este programa te permitirá generar contraseñas seguras con diferentes configuraciones.")

    while True:
        mostrar_menu()

        # Preguntar si el usuario quiere generar otra contraseña
        otra_vez = input("\n¿Quieres generar otra contraseña? (s/n): ").lower()
        if otra_vez != 's':
            print("Gracias por usar el generador de contraseñas")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()