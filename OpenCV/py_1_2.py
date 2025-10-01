# image dimension

import cv2
image = cv2.imread("python_code.png")

if image is not None:
    # channels, grayscale mai nhi milega
    height, width, channels = image.shape
    print(f"Image Loaded:\nHeight: {height}\nWidth: {width}\nChannels: {channels}")
else:
    print("Could not load image")


# grayscale conversion
if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    cv2.imshow("Gray Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()