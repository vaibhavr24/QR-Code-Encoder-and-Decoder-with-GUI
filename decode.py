from qrc import *
import cv2
d = cv2.QRCodeDetector()

val, point, str_rq = d.detectAndDecode(cv2.imread('info.jpg'))
print(val)
