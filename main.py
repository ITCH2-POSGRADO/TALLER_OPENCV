from opencv
import easyocr

#lector = easyocr.Reader(["es"],gpu=False)

image = cv2.imread("img.png")

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()