def busqueda_exhaustiva_primero_profundidad(posicion_actual, profundidad_actual, ruta_actual, mejor_ruta, profundidad_maxima):
    # Verificar si la posición actual es la nueva ubicación "A"
    if posicion_actual == "A":
        mejor_ruta.extend(ruta_actual)  # Actualizar la mejor ruta
        return
    
    # Verificar si se alcanzó la profundidad máxima
    if profundidad_actual > profundidad_maxima:
        return
    
    # Movimientos exploratorios posibles
    movimientos = [1, -1]  # Movimiento hacia la derecha o hacia la izquierda
    
    # Realizar la búsqueda exhaustiva primero en profundidad
    for movimiento in movimientos:
        nueva_posicion = posicion_actual + movimiento
        ruta_actual.append(movimiento)
        
        # Llamada recursiva con la nueva posición y profundidad incrementada
        busqueda_exhaustiva_primero_profundidad(nueva_posicion, profundidad_actual + 1, ruta_actual, mejor_ruta, profundidad_maxima)
        
        ruta_actual.pop()  # Backtracking (eliminar el último movimiento de la ruta actual)


# Función principal
def buscar_nueva_ubicacion():
    posicion_inicial = "B"
    profundidad_maxima = 6  # Profundidad máxima deseada
    
    ruta_actual = []  # Lista para almacenar la ruta actual
    mejor_ruta = []  # Lista para almacenar la mejor ruta encontrada
    
    busqueda_exhaustiva_primero_profundidad(posicion_inicial, 0, ruta_actual, mejor_ruta, profundidad_maxima)
    
    # Imprimir la mejor ruta encontrada
    print("Mejor ruta encontrada:", mejor_ruta)


# Llamar a la función principal
buscar_nueva_ubicacion()