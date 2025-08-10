"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/tests/test_tablero.py".
"""

## Inicio del código.

# Inicio de imports.

import unittest
from src.tablero import Tablero, CeldaOcupadaException

# Fin de imports.

# Inicio de la clase de pruebas.

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_inicializacion_vacia(self):
        for fila in self.tablero.contenedor:
            for celda in fila:
                self.assertEqual(celda, " ", "La celda debería estar vacía al inicio.")

    def test_colocar_ficha_valida(self):
        self.tablero.colocar_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_celda_ocupada(self):
        self.tablero.colocar_ficha(1, 1, "O")
        with self.assertRaises(CeldaOcupadaException):
            self.tablero.colocar_ficha(1, 1, "X")

    def test_verificar_ganador_fila(self):
        for col in range(3):
            self.tablero.colocar_ficha(0, col, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))

    def test_verificar_ganador_columna(self):
        for fila in range(3):
            self.tablero.colocar_ficha(fila, 0, "O")
        self.assertTrue(self.tablero.verificar_ganador("O"))

    def test_verificar_ganador_diagonal(self):
        for i in range(3):
            self.tablero.colocar_ficha(i, i, "X")
        self.assertTrue(self.tablero.verificar_ganador("X"))

    def test_tablero_lleno(self):
        ficha = "X"
        for fila in range(3):
            for col in range(3):
                self.tablero.colocar_ficha(fila, col, ficha)
                ficha = "O" if ficha == "X" else "X"
        self.assertTrue(self.tablero.tablero_lleno())

# Fin de la clase de pruebas.

if __name__ == "__main__":
    unittest.main()

## Fin del código.