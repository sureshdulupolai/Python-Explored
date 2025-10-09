import cv2

def moving_text():
    cap = cv2.VideoCapture(0)
    print("✅ Press 'q' to exit text animation window.")

    x = 0
    y = 50
    direction = 5

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.putText(frame, "Spyn Technologies", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3, cv2.LINE_AA)

        x += direction
        if x > frame.shape[1] - 300 or x < 0:
            direction = -direction

        cv2.imshow("Fun Text Animation - Spyn Technologies", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    moving_text()
