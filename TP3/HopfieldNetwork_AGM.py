import numpy as np


class HopfieldNetwork_AGM:
    def __init__(self, numero_neuronas):
        """
        Inicializa la red de Hopfield

        Args:
            numero_neuronas: Es el número de neuronas en la red de Hopfield
        """
        self.numero_neuronas = numero_neuronas
        self.pesos = np.zeros((self.numero_neuronas, self.numero_neuronas))

    def entrenar_hebb(self, data_entrenamiento):
        """
                Entrena al modelo de Hopfield usando el método de Hebb
        |
                Args:
                    data_entrenamiento: Es un listado de vectores binarios, donde cada vector binario representa un ejemplo de entrenamiento
        """
        for ejemplo in data_entrenamiento:
            x = np.reshape(ejemplo.flatten(), (self.numero_neuronas, 1))
            self.pesos += np.dot(x, x.T) / self.numero_neuronas

        # Establece la diagonal principal de los pesos como cero
        np.fill_diagonal(self.pesos, 0)

    def entrenar_pseudoinversa(self, data_entrenamiento):
        """
        Entrena al modelo de Hopfield usando el método de Pseudoinverso

        Args:
            data_entrenamiento: Es un listado de vectores binarios, donde cada vector binario representa un ejemplo de entrenamiento
        """
        # Calcula el pseudoinverso de los datos de entrenamiento y asigna los valores a la red
        num_ejemplos = len(data_entrenamiento)
        datos_apilados = np.vstack(data_entrenamiento)
        self.pesos = np.linalg.pinv(
            datos_apilados.T @ datos_apilados
            - num_ejemplos * np.eye(self.numero_neuronas)
        )

    def predecir(self, data_prueba):
        """
        Predice la salida de la red de Hopfield dados datos de prueba

        Args:
            data_prueba: Es un vector binario donde cada valor binario representa un ejemplo de prueba.
        """
        salida = np.dot(self.pesos, data_prueba)
        return np.sign(salida)
