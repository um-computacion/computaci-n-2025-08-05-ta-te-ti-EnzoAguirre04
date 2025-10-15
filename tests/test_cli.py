"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/tests/test_cli.py".
"""

## Inicio del código.

# Inicio de imports.

import unittest
from unittest.mock import patch
from io import StringIO
from src.cli import ejecutar_juego

# Fin de imports.

# Inicio de la clase de pruebas.

class TestCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        'Ana',       # Nombre jugador 1
        'z', 'X',    # Ficha inválida 'z' -> válida 'X'
        'Beto',      # Nombre jugador 2
        'O',         # Ficha jugador 2
        '0 0', '1 1', '0 1', '1 0', '0 2'  # Jugadas para ganar Ana
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_ficha_invalida_y_juego(self, mock_stdout, mock_input):
        ejecutar_juego()
        salida = mock_stdout.getvalue()
        self.assertIn("Ficha inválida", salida)
        self.assertIn("¡Ana ganó con la ficha 'X'!", salida)

    @patch('builtins.input', side_effect=[
        'Ana',
        'X',
        'Beto',
        'O',
        '0 0',       # Jugada válida
        '0 0',       # Celda ocupada, debe pedir de nuevo
        '1 1',       # Jugada válida
        '0 1',
        '1 0',
        '0 2'
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_jugada_celda_ocupada(self, mock_stdout, mock_input):
        ejecutar_juego()
        salida = mock_stdout.getvalue()
        self.assertIn("La celda (0, 0) ya está ocupada", salida)

# Fin de la clase de pruebas.

if __name__ == "__main__":
    unittest.main()

## Fin del código.