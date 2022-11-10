#Umbralizacion o thresholding

#metodo de segmentacion mas basico
#fondo diferenciable entre objetos
#Compara el valor de cada pixel con el valor del umbral que le hayamos pasado

import cv2
import numpy as np

imagen = cv2.imread('imagen2.png',0)
hola ,Trunc = cv2.threshold(imagen, 250,255, cv2.THRESH_TRUNC)
hola ,Trunc = cv2.threshold(imagen, 250,255, cv2.TH)
 
cv2.imshow('Imagen', imagen)
cv2.imshow('Tipos', Trunc)
cv2.waitKey(0)
cv2.destroyAllWindows()