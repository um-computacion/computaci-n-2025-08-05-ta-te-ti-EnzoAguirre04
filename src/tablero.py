"""
Computación I - Juego de Ta-Te-Ti.
Nombre y Apellido: Enzo Agustín Aguirre Polenta.
Ciclo Lectivo: 2025.
Carrera: Ingeniería en Informática.
Ruta: "computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/src/tablero.py".
"""

### Inicio del código.

## Incio de imports.

## Fin de imports.

## Inicio de exepciones.

class CeldaOcupadaException(Exception):
    """Se intentó colocar una ficha en una celda que ya está ocupada."""
    pass

## Fin de exepciones.

## Inicio de la clase Tablero.

class Tablero:
    def __init__(self):
        # Crea el tablero 3x3 vacío.
        self.contenedor = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def imprimir(self):
        # Imprime índices columnas
        print("   0   1   2")
        for i, fila in enumerate(self.contenedor):
            # Imprime índice fila y celdas separadas con espacios y barras verticales
            print(f"{i}  " + " | ".join(fila))
            if i < 2:
                print("  " + "---+---+---")

    def validar_ficha(self, ficha):
        if ficha not in ("X", "O"):
            raise ValueError(f"Ficha inválida: {ficha}. Debe ser 'X' u 'O'.")

    def validar_posicion(self, fil, col):
        if not (0 <= fil < 3 and 0 <= col < 3):
            raise IndexError(f"Posición inválida: ({fil}, {col})")

    def celda_libre(self, fil, col):
        self.validar_posicion(fil, col)
        return self.contenedor[fil][col] == " "

    def colocar_ficha(self, fil, col, ficha):
        # Coloca la ficha si está libre. Lanza excepciones si hay problemas.
        self.validar_posicion(fil, col)
        self.validar_ficha(ficha)

        if not self.celda_libre(fil, col):
            raise CeldaOcupadaException(f"La celda ({fil}, {col}) ya está ocupada.")

        self.contenedor[fil][col] = ficha

    def verificar_ganador(self, ficha):
        # Verifica si hay una línea completa con la ficha dada.
        self.validar_ficha(ficha)

        # Filas
        for fil in self.contenedor:
            if all(c == ficha for c in fil):
                return True

        # Columnas
        for col in range(3):
            if all(self.contenedor[f][col] == ficha for f in range(3)):
                return True

        # Diagonales
        if all(self.contenedor[i][i] == ficha for i in range(3)):
            return True
        if all(self.contenedor[i][2 - i] == ficha for i in range(3)):
            return True

        return False

    def tablero_lleno(self):
        # Devuelve True si no hay espacios vacíos.
        return all(self.contenedor[f][c] != " " for f in range(3) for c in range(3))

## Fin de la clase Tablero.

### Fin del código.