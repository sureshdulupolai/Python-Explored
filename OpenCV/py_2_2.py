# Cropping Images using Slicing in OpenCV
# cropped_image = image[startY:endY, startX:endX]

# border cutting => badi img se choti photo nikalna 
"""
 
-> = x-axis
| = y-axis

x = 400 px
y = 300 px
each row = 1 px -> basic

x = 0, 1, ... 399. 
y = 0,1, ... 299. 
because it srating from 0

y axis = row = top to bottom
x axis = column = left to right

image[startY:endY, startX:endX]
startY = 100
endY = 200
startX = 50
endX = 150

100:200 
50:150

| y axis = 100 to 200
- x axis = 50 to 150

button actual image is 0 to 200 y axis, and x axis = 0 to 399
inside that it cut a 100 to 200 part and 50 to 150

"""

import cv2

image = cv2.imread("python_code.png")

if image is not None:
    cropped = image[100:200, 50:150]
    cv2.imshow("Orginal Image", image)
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Not Loaded...")
