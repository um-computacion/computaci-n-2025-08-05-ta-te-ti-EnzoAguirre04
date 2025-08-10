# Juego de Ta-te-tí

---

## Estructura de archivos:

```
tateti/
│
├── main.py
│
├── src/
│ ├── init.py
│ ├── cli.py
│ ├── jugador.py
│ ├── tablero.py
│ └── tateti.py
│
├── tests/
│ ├── init.py
│ ├── test_cli.py
│ ├── test_jugador.py
│ ├── test_tablero.py
│ └── test_tateti.py
│
├── docs/
│ └── documentation.md
│
└── README.md
```

---

## Guía de ejecución:

### Requisitos previos:

- Python 3.10 o superior instalado.
- Ejecutar desde la raíz del proyecto `computaci-n-2025-08-05-ta-te-ti-EnzoAguirre04/`.

### Ejecutar el juego:

Desde la terminal, correr:

```bash
python main.py
```

Se abrirá el archivo main, en forma de menú, y con las siguientes opciones:

```
¿Qué querés hacer?
1 - Jugar Ta-te-ti
2 - Ejecutar tests
0 - Salir
```

Si se selecciona la opción "2", se abre el siguiente submenú:

```
Seleccioná qué test ejecutar:
1 - Test CLI
2 - Test Jugador
3 - Test Tablero
4 - Test Tateti
0 - Volver
```