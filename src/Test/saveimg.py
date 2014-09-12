#encoding:gb2312
import cv2
import sys

img=cv2.imread(sys.argv[1])
#cv2.namedWindow("Image")
#cv2.imshow("Image",img)
cv2.imwrite(sys.argv[2]+"1.jpg",img)
#cv2.waitKey(0)