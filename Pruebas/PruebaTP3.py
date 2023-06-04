import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog

from PIL import Image


class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, images):
        for image in images:
            if image is not None:
                image = image.reshape(-1)
                self.weights += np.outer(image, image)

    def predict(self, image):
        if image is not None:
            image = image.reshape(-1)
            output = np.zeros(self.n_neurons)
            for i in range(self.n_neurons):
                for j in range(self.n_neurons):
                    output[i] += self.weights[i, j] * image[j]
            output = np.sign(output)
            return output


def main():
    folder = filedialog.askdirectory()
    images = []
    for image in os.listdir(folder):
        image = plt.imread(os.path.join(folder, image))
        image = image.mean(axis=2)
        image = Image.fromarray(image)
        image = image.thumbnail((10, 10))
        images.append(image)

    n_neurons = 100
    network = HopfieldNetwork(n_neurons=n_neurons)
    network.train(images)

    test_image = filedialog.askopenfilename()
    if test_image is not None:
        test_image = Image.open(test_image)
        test_image = test_image.thumbnail((10, 10))
        output = network.predict(test_image)

        center = np.argmax(output)
        if test_image is not None:
            x, y = center // test_image.width, center % test_image.width
        else:
            x, y = None, None
        print(x, y)


if __name__ == "__main__":
    main()
