# Proyecto-Integrador-Joel-Auad
Proyecto integrador
* **Integrantes:** Joel Isaias Auad Sánchez
Fecha: Octubre 2026

## Objetivo del Sistema
Desarrollar una aplicación de escritorio interactiva en Python utilizando la librería Tkinter para permitir que dos usuarios jueguen partidas de Piedra, Papel o Tijera por turnos, gestionando de forma automática el marcador acumulado y la continuidad de las rondas.

## Descripción de Funcionalidades
* **Interfaz Gráfica Básica:** Ventana de escritorio intuitiva construida con Tkinter, libre de complejidades visuales o dependencias externas.
* **Sistema de 2 Jugadores por Turnos:** Oculta de manera lógica la elección del primer usuario para asegurar la confidencialidad de su jugada antes de que el segundo usuario seleccione la suya.
* **Marcador en Tiempo Real:** Actualiza de forma inmediata las victorias de cada usuario tras evaluar las reglas clásicas del juego.
* **Control de Continuidad:** Al finalizar cada ronda, muestra de manera directa botones de decisión ("Sí" / "No") para continuar jugando o cerrar el programa.

## Arquitectura y Flujo del Sistema
* **Arquitectura:** Estructura modular lineal basada en funciones de control de estado (`turno`, `eleccion1`) y gestión de eventos de interfaz mediante Tkinter.
* **Funcionalidad (Flujo):** 
  1. Inicio de ronda con el turno del Usuario 1.
  2. Selección de opción (Piedra, Papel o Tijera) y cambio automático al turno del Usuario 2.
  3. Evaluación de resultados, actualización del marcador global y bloqueo temporal de botones de juego.
  4. Consulta interactiva de continuidad ("¿Jugar otra ronda?").
