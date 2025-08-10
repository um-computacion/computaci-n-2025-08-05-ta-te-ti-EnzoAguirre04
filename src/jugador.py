"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/src/jugador.py".
"""

### Inicio del código.

## Incio de imports.

## Fin de imports.

## Inicio de exepciones.

class FichaInvalidaError(Exception):
    """Se lanza cuando la ficha no es 'X' ni 'O'."""
    pass


class JugadaInvalidaError(Exception):
    """Se lanza cuando la jugada ingresada no cumple el formato o el rango."""
    pass

## Fin de exepciones.

## Inicio de la clase Jugador.

class Jugador:
    def __init__(self, nombre, ficha):
        if ficha not in ("X", "O"):
            raise FichaInvalidaError(f"Ficha inválida: {ficha}. Debe ser 'X' u 'O'.")
        self.nombre = nombre
        self.ficha = ficha

    def pedir_jugada(self):
        """
        Solicita al usuario que ingrese fila y columna.
        Devuelve una tupla (fila, columna) con índices enteros 0–2.
        """
        while True:
            try:
                entrada = input(f"{self.nombre} ({self.ficha}), ingrese fila y columna (0-2) separadas por espacio: ")
                fil_str, col_str = entrada.strip().split()
                fil, col = int(fil_str), int(col_str)

                if not (0 <= fil < 3 and 0 <= col < 3):
                    raise JugadaInvalidaError("Posición fuera de rango. Debe estar entre 0 y 2.")

                return fil, col

            except ValueError:
                print("Formato inválido. Ejemplo: '1 2'")
            except JugadaInvalidaError as e:
                print(e)

## Fin de la clase Jugador.

### Fin del código.