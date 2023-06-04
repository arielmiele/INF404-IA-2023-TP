import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image
import numpy as np
from HopfieldNetwork_AGM import HopfieldNetwork_AGM
from utils_imagenes import cargar_datos_entrenamiento, guardar_datos_entrenamiento
from skimage.util import img_as_float


def seleccionar_carpeta_entrenamiento():
    root = tk.Tk()
    root.withdraw()
    carpeta_entrenamiento = fd.askdirectory(
        parent=root,
        initialdir="/",
        title="Seleccione la carpeta de datos de entrenamiento",
    )
    root.destroy()
    return carpeta_entrenamiento


def seleccionar_imagen_prueba():
    root = tk.Tk()
    root.title("Selección de Imagen")
    root.resizable(False, False)
    root.geometry("300x150")

    filetypes = (
        ("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp"),
        ("Todos los archivos", "*.*"),
    )

    imagen_prueba = fd.askopenfilename(
        initialdir="/", title="Seleccione una imagen de prueba", filetypes=filetypes
    )

    showinfo(title="Archivo seleccionado", message=imagen_prueba)

    root.destroy()
    return imagen_prueba


def entrenar_hopfield(datos_entrenamiento, metodo):
    num_neuronas = datos_entrenamiento[0].shape[0] * datos_entrenamiento[0].shape[1]
    red_hopfield = HopfieldNetwork_AGM(num_neuronas)
    if metodo == "hebb":
        red_hopfield.entrenar_hebb(datos_entrenamiento)
    elif metodo == "pseudoinversa":
        red_hopfield.entrenar_pseudoinversa(datos_entrenamiento)
    else:
        raise ValueError("Método de entrenamiento no válido")
    return red_hopfield


def predecir_coordenadas(red_hopfield, datos_prueba):
    """
    Esta función usa la red de Hopfield para predecir las coordenadas X e Y de un anillo en una imagen de prueba.
    Primero convierte la imagen en un array de NumPy.
    Luego, predice la salida usando la red de Hopfield.
    La función devuelve una tupla, donde el primer elemento es la coordenada X y el segundo la coordenada Y.
    """
    datos_prueba = datos_prueba.flatten()
    prediccion = red_hopfield.predecir(datos_prueba)
    indice_maximo = np.argmax(prediccion)
    coordenada_x = indice_maximo % 10
    coordenada_y = indice_maximo // 10
    return coordenada_x, coordenada_y


if __name__ == "__main__":
    """
    Función principal (main) del programa.
    La función primero crea una ventana Tkinter.
    Luego, la función muestra una ventana donde el usuario puede seleccionar la carpeta donde se encuentran almacenados los datos de entrenamiento.
    Finalmente, la función carga los datos de entrenamiento, entrena a la red de Hopfield y
      predice el valor de las coordenadas de X e Y de un anillo perteneciente a una imagen de prueba.
    """

    carpeta_entrenamiento = seleccionar_carpeta_entrenamiento()
    datos_entrenamiento = cargar_datos_entrenamiento(carpeta_entrenamiento)
    guardar_datos_entrenamiento(datos_entrenamiento)

    metodo_entrenamiento = input(
        "Seleccione el método de entrenamiento (hebb/pseudoinversa): "
    )

    red_hopfield = entrenar_hopfield(datos_entrenamiento, metodo_entrenamiento)

    imagen_prueba = seleccionar_imagen_prueba()
    print(imagen_prueba)
    imagen = Image.open(imagen_prueba)
    imagen = imagen.resize((10, 10))
    datos_prueba = img_as_float(imagen)

    coordenada_x, coordenada_y = predecir_coordenadas(red_hopfield, datos_prueba)

    print("La coordenada X del anillo es:", coordenada_x)
    print("La coordenada Y del anillo es:", coordenada_y)
