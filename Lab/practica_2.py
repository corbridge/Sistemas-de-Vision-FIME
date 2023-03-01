import cv2          #Se cargan las librerias 
import numpy as np
import practica_1


FILE_NAME = r'fotos\D1.png'  #Se carga la imagen 

practica_1.make_image_scale(FILE_NAME, 5)   #Aqui se coloca que tanto se quiere pixelear la imagen 
practica_1.get_matrix()                     #En esta parte se muestar la matriz de la imagen 
try:
   
    img = cv2.imread('scaled.png')          #Aqui guardamos la imagen escalda o pixeleada anteriormente 

    edges = cv2.Canny(img, 100, 200)        #Con esta linea logramos que se destaquen los contornos de la imagen 

    cv2.imwrite('result.png', edges)        #Mostrar la imagen reultante 
except IOError:
    print ('Error !!!')

