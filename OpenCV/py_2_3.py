# image rotation and flipping

# M = cv2.getRotationMatrix2D(center, angle, scale)
# rotate_image = cv2.warpAffine(image, M, (width, height))


import cv2
image = cv2.imread("python_code.png")
