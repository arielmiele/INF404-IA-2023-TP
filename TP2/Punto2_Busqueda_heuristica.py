import heapq

# Definir la función heurística
def funcionHeuristica(posicion):
    # Calcular la distancia heurística desde la posición actual hasta la meta
    distancia = abs(posicion - 'A')
    return distancia

# Implementar la búsqueda heurística
def busquedaHeuristica(posicionInicial):
    # Crear una cola de prioridad (heap) para almacenar los nodos a explorar
    colaPrioridad = []
    heapq.heappush(colaPrioridad, (funcionHeuristica(posicionInicial), [posicionInicial], 0))

    while colaPrioridad:
        # Extraer el nodo de mayor prioridad (menor valor heurístico)
        _, rutaActual, profundidad = heapq.heappop(colaPrioridad)
        posicionActual = rutaActual[-1]

        # Verificar si la posición actual es la nueva ubicación "A"
        if posicionActual == 'A':
            return rutaActual

        # Verificar la profundidad máxima
        if profundidad < 6:
            # Movimientos exploratorios posibles
            movimientos = [1, -1]  # Movimiento hacia la derecha o hacia la izquierda

            # Explorar los movimientos posibles
            for movimiento in movimientos:
                nuevaPosicion = posicionActual + movimiento
                nuevaRuta = rutaActual + [nuevaPosicion]
                nuevaProfundidad = profundidad + 1

                # Calcular el valor heurístico para la nueva posición
                valorHeuristico = funcionHeuristica(nuevaPosicion)

                # Agregar el nodo a la cola de prioridad
                heapq.heappush(colaPrioridad, (valorHeuristico, nuevaRuta, nuevaProfundidad))

    return None  # No se encontró una ruta hacia la meta

# Ejemplo de uso
posicionInicial = 'B'
rutaOptima = busquedaHeuristica(posicionInicial)

if rutaOptima:
    print("Ruta óptima encontrada:", rutaOptima)
else:
    print("No se encontró una ruta óptima hacia la meta.")
