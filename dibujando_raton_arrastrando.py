import cv2
import numpy as np

#Definimos la funcion para dibujar con el raton
def dibujar(evento,x,y,etiquetas,parametros):
    global dibujando, valorx, valory
    if evento == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        valorx = x
        valory = y
    elif evento == cv2.EVENT_MOUSEMOVE:
        if dibujando == True:
            cv2.rectangle(imagen,(valorx,valory),(x,y),(255,0,0),-1)
    elif evento == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(imagen,(valorx,valory),(x,y),(255,0,0),-1)

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