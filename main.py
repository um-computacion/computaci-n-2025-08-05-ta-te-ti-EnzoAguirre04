"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/main.py".
"""

### Inicio del código.

## Inicio de imports.

import unittest
from src.cli import ejecutar_juego

## Fin de imports.

## Inicio de la Ejecución del Menú.

# Inicio del Menú secundario para seleccionar y ejecutar tests.

def seleccionar_y_ejecutar_tests():
    test_map = {
        "1": "tests.test_cli",
        "2": "tests.test_jugador",
        "3": "tests.test_tablero",
        "4": "tests.test_tateti",
    }

    while True:
        print("\nSeleccioná qué test ejecutar:")
        print("1 - Test CLI")
        print("2 - Test Jugador")
        print("3 - Test Tablero")
        print("4 - Test Tateti")
        print("0 - Volver")
        opcion = input("Ingresá el número de la opción: ").strip()

        if opcion == "0":
            break
        elif opcion in test_map:
            suite = unittest.defaultTestLoader.loadTestsFromName(test_map[opcion])
            runner = unittest.TextTestRunner(verbosity=2)
            resultado = runner.run(suite)

            if resultado.wasSuccessful():
                print("Todos los tests pasaron correctamente.")
            else:
                print("Algunos tests fallaron.")
        else:
            print("Opción inválida, probá de nuevo.")

# Fin del Menú secundario para seleccionar y ejecutar tests.

# Inico del Menú principal para ejecutar el juego o tests.

def menu_principal():
    while True:
        print("\n¿Qué querés hacer?")
        print("1 - Jugar Ta-te-ti")
        print("2 - Ejecutar tests")
        print("0 - Salir")
        opcion = input("Ingresá el número de la opción: ").strip()

        if opcion == "1":
            ejecutar_juego()
        elif opcion == "2":
            seleccionar_y_ejecutar_tests()
        elif opcion == "0":
            print("Saliendo del programa. ¡Chau!")
            break
        else:
            print("Opción inválida, probá de nuevo.")

if __name__ == "__main__":
    menu_principal()

# Fin del Menú principal para ejecutar el juego o tests.

## Fin de la Ejecución del Menú.

### Fin del código.