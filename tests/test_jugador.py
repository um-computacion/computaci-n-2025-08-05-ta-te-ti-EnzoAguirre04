"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/tests/test_jugador.py".
"""

## Inicio del código.

# Inicio de imports.

import unittest
from src.jugador import Jugador, FichaInvalidaException

# Fin de imports.

# Inicio de la clase de pruebas.

class TestJugador(unittest.TestCase):

    def test_creacion_jugador_valida(self):
        j1 = Jugador("Ana", "X")
        self.assertEqual(j1.ficha, "X")

        j2 = Jugador("Beto", "o")  # minúscula
        self.assertEqual(j2.ficha, "O")

        j3 = Jugador("Caro", "0")  # cero
        self.assertEqual(j3.ficha, "O")

    def test_ficha_invalida(self):
        with self.assertRaises(FichaInvalidaException):
            Jugador("David", "Z")

        with self.assertRaises(FichaInvalidaException):
            Jugador("Eva", "")

# Fin de la clase de pruebas.

if __name__ == "__main__":
    unittest.main()

## Fin del código.