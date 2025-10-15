"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/src/tateti.py".
"""

### Inicio del código.

## Incio de imports.

from src.tablero import Tablero, CeldaOcupadaException
from src.jugador import Jugador

## Fin de imports.

## Inicio de exepciones.

class JugadaInvalidaException(Exception):
    """Se intentó hacer una jugada fuera del tablero."""
    pass

## Fin de exepciones.

## Inicio de la clase Tateti.

class Tateti:
    def __init__(self, jugador1: Jugador, jugador2: Jugador):
        if jugador1.ficha == jugador2.ficha:
            raise ValueError("Los jugadores no pueden tener la misma ficha.")

        self.tablero = Tablero()
        self.jugadores = [jugador1, jugador2]
        self.turno_actual = 0  # índice del jugador que juega
        self.ganador = None

    def jugador_actual(self) -> Jugador:
        return self.jugadores[self.turno_actual]

    def jugar_turno(self, fil: int, col: int) -> None:
        jugador = self.jugador_actual()
        try:
            self.tablero.colocar_ficha(fil, col, jugador.ficha)
        except IndexError:
            raise JugadaInvalidaException(f"Posición inválida: ({fil}, {col})")
        except CeldaOcupadaException as e:
            raise e

        if self.tablero.verificar_ganador(jugador.ficha):
            self.ganador = jugador

        elif self.tablero.tablero_lleno():
            self.ganador = None  # Empate, nadie gana

        else:
            self.turno_actual = 1 - self.turno_actual  # Cambiar turno

    def juego_terminado(self) -> bool:
        return self.ganador is not None or self.tablero.tablero_lleno()

## Fin de la clase Tateti.

### Fin del código.