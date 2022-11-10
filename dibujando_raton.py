import cv2
import numpy as np

#Definimos la funcion para dibujar con el raton
def dibujar(evento,x,y,etiquetas,parametros):
    if evento == cv2.EVENT_LBUTTONDOWN:#Si clickea el boton iszquierdo, este dibuje
        cv2.circle(imagen, (x,y),50,(255,0,0),-1)#Dibujamos un circulo con radio 50 y relleno

#Conectamos la imagen con la funcion dibujar
cv2.namedWindow(winname='Imagen')#Vamos a conectar una ventana llamada imagen
cv2.setMouseCallback('Imagen', dibujar)#Cuando se pulse el boton en la ventana  llamada imagen mande a llamar dibujar

#Mostramos constantemente la imagen donde vamos a dibujar
imagen = np.zeros((512, 512, 3), dtype = "uint8")
while True:
    cv2.imshow('Imagen', imagen)
    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        break