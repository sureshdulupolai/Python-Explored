# Resizing & Scalling Images - cv2.resize()
# resized = cv2.resize(src, dsize, fx, fy, interpolation)

"""

cv2 = libary 
resize = func
src = image
dsize = width & height
fx, fx, inter = optional

"""

import cv2

image = cv2.imread("python_code.png")

if image is not None:
    print('Image Loaded Successfully!!!')
    resized = cv2.resize(image, (300, 300)) # src, widht, height
    cv2.imshow("Orginal Image", image)
    cv2.imshow("Resized Image", resized)

    cv2.imwrite("resized_image.png", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print('Image not loaded...')