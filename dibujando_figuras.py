import numpy as np
import cv2

imagen = cv2.imread('imagen2.png')
print(imagen.shape)



#NOTA: las cordenadas son de la esquina superior izquierda como eje 0,0
#El punto uno es la esquina superior izq y el punto dos esq inferior derecha, thicnkess es el grosor

#Rectangulo
#cv2.rectangle(imagen, pt1 = (), pt2 = (), color = (255,255,255), thickness=10)
cv2.rectangle(imagen, pt1=(20,20), pt2=(100,100), color=(255,0,0),thickness=10)

#Circulo
#Centro en 250,250, radio de 100,
cv2.circle(imagen, center = (250,250), radius=100, color=(0,255,0), thickness=10)

#Linea
#punto origen, punto final, podemos obtener el tamaño de la imagen, con el shape
print(imagen.shape[1])
cv2.line(imagen, pt1=(0,400), pt2=(imagen.shape[1],300), color = (0,0,255), thickness=10)


cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()