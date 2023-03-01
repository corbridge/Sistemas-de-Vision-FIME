import cv2
import numpy as np
import practica_1


FILE_NAME = r'fotos\g.png'

practica_1.make_image_scale(FILE_NAME, 5)
try:
    # Read image from disk.
    img = cv2.imread('scaled.png')

    # Canny edge detection.
    edges = cv2.Canny(img, 100, 200)

    # Write image back to disk.
    cv2.imwrite('result.png', edges)
except IOError:
    print ('Error while reading files !!!')

