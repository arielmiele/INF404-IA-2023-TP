import os.path
from PIL import Image
import numpy as np
from skimage.util import img_as_float


def cargar_datos_entrenamiento(carpeta_entrenamiento):
    """
    Esta función lee los datos de entrenamiento desde una carpeta de imagenes.
    Devuelve una lista de arrays de NumPy, donde cada array representa una imagen.
    """
    datos_entrenamiento = []
    for archivo_imagen in os.listdir(carpeta_entrenamiento):
        imagen = Image.open(os.path.join(carpeta_entrenamiento, archivo_imagen))
        imagen = imagen.resize((10, 10))
        datos_imagen = img_as_float(imagen)
        # print(datos_imagen)
        # datos_imagen = np.array(imagen)
        datos_entrenamiento.append(datos_imagen)

    # Redimensionar todas las imágenes a un tamaño común
    forma_comun = datos_entrenamiento[0].shape
    datos_entrenamiento = [
        np.resize(imagen, forma_comun) for imagen in datos_entrenamiento
    ]

    return datos_entrenamiento


def guardar_datos_entrenamiento(datos_entrenamiento):
    """
    Esta función guarda los datos de entrenamiento como un archivo.
    Los datos de entrenamiento son una lista de arrays de NumPy, donde cada array representa una imagen.
    La función almacena los datos en un archivo llamado `datos_de_entrenamiento.npy`.
    """
    datos_apilados = np.stack(datos_entrenamiento)  # Apilar los arrays en uno solo
    np.save("datos_de_entrenamiento.npy", datos_apilados)
