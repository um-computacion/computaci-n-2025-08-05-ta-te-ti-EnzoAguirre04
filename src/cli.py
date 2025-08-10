"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/src/cli.py".
"""

### Inicio del código.

## Incio de imports.

from src.jugador import Jugador, FichaInvalidaException, JugadaInvalidaException
from src.tateti import Tateti
from src.tablero import CeldaOcupadaException

## Fin de imports.

## Inicio de exepciones.

## Fin de exepciones.

## Inicio del cli.

def ficha_valida(nombre_jugador):
    while True:
        ficha = input(f"Ficha del jugador {nombre_jugador} (X/O): ").strip().upper().replace("0", "O")
        if ficha not in ('X', 'O'):
            print(f"Error en la creación del jugador: Ficha inválida: {ficha}. Debe ser 'X' u 'O'.")
        else:
            return ficha

def ejecutar_juego():
    try:
        nombre1 = input("Nombre del jugador 1: ").strip()
        ficha1 = ficha_valida(nombre1)
        jugador1 = Jugador(nombre1, ficha1)

        nombre2 = input("Nombre del jugador 2: ").strip()
        while True:
            ficha2 = ficha_valida(nombre2)
            if ficha2 == ficha1:
                print(f"La ficha '{ficha2}' ya está tomada por {nombre1}. Elegí otra.")
            else:
                break
    
        jugador2 = Jugador(nombre2, ficha2)
        juego = Tateti(jugador1, jugador2)

    except FichaInvalidaException as e:
        print(f"Error en la creación del jugador: {e}")
        return

    except ValueError as e:
        print(f"Error: {e}")
        return

    while not juego.juego_terminado():
        juego.tablero.imprimir()
        jugador = juego.jugador_actual()
        while True:
            try:
                fila, col = jugador.pedir_jugada()
                juego.jugar_turno(fila, col)
                break
            except (JugadaInvalidaException, CeldaOcupadaException) as e:
                print(f"Error: {e}")

    juego.tablero.imprimir()

    if juego.ganador is None:
        print("El juego terminó en empate.")
    else:
        print(f"¡{juego.ganador.nombre} ganó con la ficha '{juego.ganador.ficha}'!")


if __name__ == "__main__":
    ejecutar_juego()

## Fin del cli.

### Fin del código.