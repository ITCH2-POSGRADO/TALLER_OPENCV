import cv2

imagen = cv2.imread('imagen.png',0)#Leemos el imread
cv2.imshow('Prueba de imagen', imagen)#Le pasamos el titulo y la variable
cv2.imwrite('Blanco.png',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()