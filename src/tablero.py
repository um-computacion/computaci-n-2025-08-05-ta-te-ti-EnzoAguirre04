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
        # Imprime en la consola el estado actual del tablero del Ta-te-ti.
        for fil in self.contenedor:
            print("|".join(fil))
            print("-" * 5)

    def celda_libre(self, fil, col):
        # Devuelve True si la celda está vacía.
        return self.contenedor[fil][col] == " "

    def colocar_ficha(self, fil, col, ficha):
        # Coloca ficha si está libre, devuelve True si pudo, False si no
        if self.celda_libre(fil, col):
            self.contenedor[fil][col] = ficha
            return True
        return False

    def verificar_ganador(self, ficha):
        # Verifica si hay una línea completa con la ficha dada

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
        # Devuelve True si no hay espacios vacíos
        return all(self.contenedor[f][c] != " " for f in range(3) for c in range(3))

## Fin de la clase Tablero.

### Fin del código.