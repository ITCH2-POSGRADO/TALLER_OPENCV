import cv2

imagen = cv2.imread('imagen2.png')

print(imagen.shape)
#Redimensionando imagenes
imagen_2 = cv2.resize(imagen,(1200,1200))
#Otra forma de redimensionar imagenes, pero ahora con porcentajes
radio_alto = 1.5
radio_ancho = 1.5
imagen_3 = cv2.resize(imagen,(0,0),imagen,radio_ancho, radio_alto)
#Volteando imagenes
imagen_4 = cv2.flip(imagen,1)
#Volteando de arriba hacia abajo
imagen_5 = cv2.flip(imagen,0)
#Pasar una imagen a escala de grises
imagen_6 = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)


#cv2.imshow('Imagen', imagen)
cv2.imshow('Imagen', imagen_6)
cv2.waitKey(0)#Si es 0, esperara una tecla, si le ponemos 10, seran 10 milisegundos, si le ponemos 1000, sera un segundo
cv2.destroyAllWindows()