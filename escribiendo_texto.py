import cv2
import numpy as np

imagen = np.zeros((512, 512, 3), dtype = "uint8")

#Agregando texto
fuente = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(imagen, text='hola', org=(20,100), fontFace=fuente, fontScale=3, color=(255,0,0),thickness=4)

#Creando poligonos
vertices = np.array([[100,300],[300,200],[400,400],[200,400]],dtype=np.int32)
print(vertices)
cv2.polylines(imagen, [vertices],isClosed=True,color=(255,255,0), thickness=5)

cv2.imshow('Imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()