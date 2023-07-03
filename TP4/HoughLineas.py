import numpy as np
import math, cv2

def transf_hough_lineas(imagen, umbral):
    # Dimensiones de la imagen
    alto, ancho = imagen.shape

    # Rango de valores de ρ y θ
    max_rho = int(math.hypot(alto, ancho))
    max_theta = 180

    # Matriz de acumulación
    acumulador = np.zeros((max_rho, max_theta))

    # Obtener los puntos de borde en la imagen
    puntos_borde = np.argwhere(imagen > 0)

    # Calcular la transformada de Hough
    for x, y in puntos_borde:
        for theta in range(max_theta):
            rho = int(x * math.cos(math.radians(theta)) + y * math.sin(math.radians(theta)))
            acumulador[rho, theta] += 1

    # Obtener las líneas detectadas por encima del umbral de votos
    lineas = np.argwhere(acumulador > umbral)

    return lineas

def draw_lineas(imagen, lineas):
    for rho, theta in lineas:
        a = np.cos(math.radians(theta))
        b = np.sin(math.radians(theta))
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(imagen, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Cargar la imagen en escala de grises
imagen = cv2.imread('C:/***/imagen.jpg', 0)

# Aplicar el detector de bordes (opcional)
bordes = cv2.Canny(imagen, 50, 150)

# Aplicar la transformada de Hough
lineas = transf_hough_lineas(bordes, umbral=100)

# Dibujar las líneas detectadas en la imagenn original
draw_lineas(imagen, lineas)

# Mostrar la imagenn con las líneas detectadas
cv2.imshow('lineas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()