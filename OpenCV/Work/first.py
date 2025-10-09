"""
Capture Video From Camera Using Python OpenCV
pip install opencv-python
"""

import cv2

# Pass one parameter:
# 0 => laptop's default webcam
# 1 => external webcam (e.g., your phone as webcam)
webcam = cv2.VideoCapture(0)

while True:
    # ret => Boolean, True if frame is captured successfully
    # frame => actual image captured from the webcam
    ret, frame = webcam.read()

    if ret == True:
        cv2.imshow("First", frame)  # Display the frame in a window
        key = cv2.waitKey(1)  # Wait for 1 millisecond for a key press

        # Stop the program if 'q' key is pressed
        if key == ord("q"):
            break

webcam.release()          # Release the webcam for other applications
cv2.destroyAllWindows()   # Close all OpenCV windows
