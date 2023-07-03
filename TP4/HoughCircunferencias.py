import numpy as np
import math, cv2

def transf_hough_circunferencias(imagen, radio_minimo, radio_maximo, umbral):
    # Dimensiones de la imagenn
    alto, ancho = imagen.shape

    # Rango de valores de x_c, y_c y r
    max_xc = ancho
    max_yc = alto
    max_r = radio_maximo - radio_minimo

    # Matriz de votación
    acumulador = np.zeros((max_yc, max_xc, max_r))

    # Obtener los puntos de borde en la imagenn
    puntos_borde = np.argwhere(imagen > 0)

    # Calcular la transformada de Hough
    for x, y in puntos_borde:
        for xc in range(max_xc):
            for yc in range(max_yc):
                for r in range(max_r):
                    radio = r + radio_minimo
                    dx = x - xc
                    dy = y - yc
                    if abs(math.hypot(dx, dy) - radio) < 1:
                        acumulador[yc, xc, r] += 1

    # Obtener las circunferencias detectadas por encima del umbral de votos
    circulos = np.argwhere(acumulador > umbral)

    return circulos

def draw_circulos(imagen, circulos, radio_minimo):
    for yc, xc, r in circulos:
        radio = r + radio_minimo
        cv2.circle(imagen, (xc, yc), radio, (0, 0, 255), 2)

# Cargar la imagenn en escala de grises
imagen = cv2.imread('imagen.jpg', 0)

# Aplicar el detector de bordes (opcional)
bordes = cv2.Canny(imagen, 50, 150)

# Aplicar la transformada de Hough
circulos = transf_hough_circunferencias(bordes, radio_minimo=10, radio_maximo=50, umbral=100)

# Dibujar las circunferencias detectadas en la imagenn original
draw_circulos(imagen, circulos, radio_minimo=10)

# Mostrar la imagenn con las circunferencias detectadas
cv2.imshow('circulos', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()