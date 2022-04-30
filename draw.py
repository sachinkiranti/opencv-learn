import numpy as np
import cv2

# img = cv2.imread('lena.jpg')

# Using numpy
img = np.zeros([512, 512, 3], np.uint8)

# Drawing a line
# Color in bgr format
img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)
img = cv2.arrowedLine(img, (0, 0), (255, 255), (147, 96, 44), 10)

# Drawing a rectangle
# If thickness is  -1 then it will fill the rectangle
img = cv2.rectangle(img, (384, 0), (512, 128), (0, 0, 255), 10)

# Drawing a circle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# Add Text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('Image Frame', img)

cv2.waitKey(0)
cv2.destroyAllWindows()