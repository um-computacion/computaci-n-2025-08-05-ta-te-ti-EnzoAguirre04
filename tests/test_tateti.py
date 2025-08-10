"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/tests/test_tateti.py".
"""

## Inicio del código.

# Inicio de imports.

import unittest
from src.tateti import Tateti
from src.jugador import Jugador, JugadaInvalidaException
from src.tablero import CeldaOcupadaException

# Fin de imports.

# Inicio de la clase de pruebas.


class TestTateti(unittest.TestCase):
    def setUp(self):
        self.jugador1 = Jugador("Ana", "X")
        self.jugador2 = Jugador("Beto", "O")
        self.juego = Tateti(self.jugador1, self.jugador2)

    def test_juego_invalido_fichas_iguales(self):
        with self.assertRaises(ValueError):
            Tateti(self.jugador1, Jugador("Carlos", "X"))

    def test_turnos_y_colocacion(self):
        self.juego.jugar_turno(0, 0)
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")
        self.assertEqual(self.juego.jugador_actual(), self.jugador2)

        self.juego.jugar_turno(1, 1)
        self.assertEqual(self.juego.tablero.contenedor[1][1], "O")
        self.assertEqual(self.juego.jugador_actual(), self.jugador1)

    def test_excepcion_celda_ocupada(self):
        self.juego.jugar_turno(0, 0)
        with self.assertRaises(CeldaOcupadaException):
            self.juego.jugar_turno(0, 0)

    def test_excepcion_jugada_invalida(self):
        with self.assertRaises(JugadaInvalidaException):
            self.juego.jugar_turno(-1, 0)

        with self.assertRaises(JugadaInvalidaException):
            self.juego.jugar_turno(0, 3)

    def test_ganador(self):
        self.juego.jugar_turno(0, 0)  # X
        self.juego.jugar_turno(1, 0)  # O
        self.juego.jugar_turno(0, 1)  # X
        self.juego.jugar_turno(1, 1)  # O
        self.juego.jugar_turno(0, 2)  # X gana

        self.assertIsNotNone(self.juego.ganador)
        self.assertEqual(self.juego.ganador, self.jugador1)
        self.assertTrue(self.juego.juego_terminado())

    def test_empate(self):
        jugadas = [
            (0, 0), (0, 1),
            (0, 2), (1, 1),
            (1, 0), (1, 2),
            (2, 1), (2, 0),
            (2, 2),
        ]
        for i, (fila, col) in enumerate(jugadas):
            self.juego.jugar_turno(fila, col)
        self.assertIsNone(self.juego.ganador)
        self.assertTrue(self.juego.juego_terminado())

# Fin de la clase de pruebas.

if __name__ == "__main__":
    unittest.main()

## Fin del código.