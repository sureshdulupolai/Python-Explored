import cv2
import numpy as np

def color_filter():
    cap = cv2.VideoCapture(0)

    print("✅ Press 'q' to exit color filter window.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to HSV (Hue-Saturation-Value)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Choose your color range (RED example)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        mask = mask1 + mask2
        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Color Filter - Red Only", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    color_filter()
