#Import libraries
import cv2
import numpy as np

#Get image
img = cv2.imread("cat.png")

#Gray out the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Blur lines
gray = cv2.medianBlur(gray, 5)

#Create the edges
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 9, 9)

#Do coloring and create the cartoon image
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

#output each section in separate windows
cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
