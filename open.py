import cv2
import easyocr

reader = easyocr.Reader(['es','en',],gpu=False)
imagen = cv2.imread('img2.png')

resultado = reader.readtext(imagen)

for res in resultado:
    print('res: ',res)
    pt0 = res[0][0]
    pt1 = res[0][1]
    pt2 = res[0][2]
    pt3 = res[0][3]

    cv2.putText(imagen, res[1],(pt0[0], pt0[1]-3),2,0.8,(0,0,0),1)
    cv2.rectangle(imagen,pt0,pt2,(166,56,242),2)
    cv2.circle(imagen, pt0,2,(255,0,0),2)
    cv2.circle(imagen, pt1,2,(255,255,0),2)
    cv2.circle(imagen, pt2,2,(0,0,255),2)
    cv2.circle(imagen, pt3,2,(0,255,0),2)



print(resultado)
cv2.imshow("Image", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()