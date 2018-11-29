import numpy as np
from scipy.misc import imshow
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
def generate_image(m, n_H, n_W, n_C):
    image = np.random.uniform(0, 255, size=[m , n_H, n_W, n_C]).astype('float32')
    return image

if __name__ == "__main__":
    image = generate_image(10,64,64,3)
    print(image)
    imshow(image[0])
    plt.show()

   